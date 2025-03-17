<?php

namespace App\Http\Controllers;

use Inertia\Inertia;
use Inertia\Response;

class TodoListController extends Controller
{
    public function index(): Response
    {
        return Inertia::render('TodoList/Index', [
            'foo' => 'bar',
        ]);
    }
}
