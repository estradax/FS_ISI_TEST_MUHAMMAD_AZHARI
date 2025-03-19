<?php

namespace App\Http\Controllers;

use const Grpc\STATUS_INVALID_ARGUMENT;
use const Grpc\STATUS_OK;

use App\GrpcGen\CreateTodoRequest;
use App\GrpcGen\DeleteTodoRequest;
use App\GrpcGen\GetTodosRequest;
use App\GrpcGen\Ordering;
use App\GrpcGen\TodoClient;
use App\GrpcGen\TodoMessage;
use App\GrpcGen\UpdateTodoRequest;
use DateTime;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class TodoListController extends Controller
{
    private TodoClient $client;

    public function __construct()
    {
        $this->client = new TodoClient(getenv('PYTHON_SERVICE'), [
            'credentials' => \Grpc\ChannelCredentials::createInsecure(),
        ]);
    }

    public function index(): Response
    {
        [$ongoingTodos, $status] = $this->getTodos(false, Ordering::ASC);
        if ($status->code !== STATUS_OK) {
            return Inertia::render('TodoList/Index', [
                'error' => 'Something went wrong, try again later.',
            ]);
        }

        [$completedTodos, $status] = $this->getTodos(true, Ordering::DESC);
        if ($status->code !== STATUS_OK) {
            return Inertia::render('TodoList/Index', [
                'error' => 'Something went wrong, try again later.',
            ]);
        }

        return Inertia::render('TodoList/Index', [
            'ongoing_todos' => $ongoingTodos,
            'completed_todos' => $completedTodos,
        ]);
    }

    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required',
        ]);

        $todoRequest = new CreateTodoRequest;
        $todoRequest->setTitle($request->title);

        [$_, $status] = $this->client->CreateTodo($todoRequest)->wait();
        if ($status->code === STATUS_INVALID_ARGUMENT) {
            return response()->json([
                'error' => $status->message,
            ], 422);
        }
        if ($status->code !== STATUS_OK) {
            return response()->json([
                'error' => 'Something went wrong, try again later.',
            ], 500);
        }

        return response()->noContent();
    }

    public function update(string $id, Request $request)
    {
        $request->validate([
            'title' => 'required',
            'is_completed' => 'required|boolean',
        ]);

        $todoRequest = new UpdateTodoRequest;
        $todoRequest->setId($id);
        $todoRequest->setTitle($request->title);
        $todoRequest->setIsCompleted($request->is_completed);

        [$_, $status] = $this->client->UpdateTodo($todoRequest)->wait();
        if ($status->code === STATUS_INVALID_ARGUMENT) {
            return response()->json([
                'error' => $status->message,
            ], 422);
        }
        if ($status->code !== STATUS_OK) {
            return response()->json([
                'error' => 'Something went wrong, try again later.',
            ], 500);
        }

        return response()->noContent();
    }

    public function destroy(string $id)
    {
        $todoRequest = new DeleteTodoRequest;
        $todoRequest->setId($id);

        [$_, $status] = $this->client->DeleteTodo($todoRequest)->wait();
        if ($status->code === STATUS_INVALID_ARGUMENT) {
            return response()->json([
                'error' => $status->message,
            ], 422);
        }
        if ($status->code !== STATUS_OK) {
            return response()->json([
                'error' => 'Something went wrong, try again later.',
            ], 500);
        }

        return response()->noContent();
    }

    private function getTodos(bool $isCompleted, int $ordering): array
    {
        $request = new GetTodosRequest;
        $request->setIsCompleted($isCompleted);
        $request->setOrdering($ordering);

        [$data, $status] = $this->client->GetTodos($request)->wait();

        $data = array_map(fn ($todo) => $this->mapTodo($todo), iterator_to_array($data->getTodos()));

        return [$data, $status];
    }

    private function mapTodo(TodoMessage $todo): array
    {
        return [
            'id' => $todo->getId(),
            'title' => $todo->getTitle(),
            'is_completed' => $todo->getIsCompleted(),
            'created_at' => $todo->getCreatedAt()->toDateTime()->format(DateTime::RFC3339),
            'updated_at' => $todo->getUpdatedAt()->toDateTime()->format(DateTime::RFC3339),
        ];
    }
}
