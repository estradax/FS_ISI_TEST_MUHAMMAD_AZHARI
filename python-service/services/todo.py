import uuid
import grpc
import logging
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from models.models import Todo
from grpc_gen.todo_pb2_grpc import TodoServicer
from grpc_gen.todo_pb2 import Ordering, TodoMessage, GetTodosResponse, CreateTodoResponse, UpdateTodoResponse, DeleteTodoResponse

logger = logging.getLogger("todo_service")

class TodoService(TodoServicer):
  def __init__(self, engine: Engine):
    self.engine = engine

  def GetTodos(self, request, context):
    logger.info("get todos with request ordering=%s is_completed=%s",
                "ASC" if request.ordering == Ordering.ASC else "DESC", request.is_completed)
    with Session(self.engine) as session:
      ordering = Todo.created_at.asc()
      if request.ordering == Ordering.DESC:
        ordering = Todo.created_at.desc()

      todos = session.query(Todo).order_by(
          ordering).filter_by(is_completed=request.is_completed)

    todos = [TodoMessage(id=todo.id, title=todo.title, is_completed=todo.is_completed,
                         created_at=todo.created_at, updated_at=todo.updated_at) for todo in todos]
    return GetTodosResponse(todos=todos)

  def CreateTodo(self, request, context):
    logger.info("create todo with request title=\"%s\"", request.title)
    if len(request.title) < 1:
      context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                    "title at least one character")

    with Session(self.engine) as session:
      session.add(Todo(id=uuid.uuid4(), title=request.title))
      session.commit()

    return CreateTodoResponse()

  def UpdateTodo(self, request, context):
    logger.info("update todo with request id=\"%s\" title=\"%s\" is_completed=%s",
                request.id, request.title, request.is_completed)
    if len(request.title) < 1:
      context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                    "title at least one character")

    with Session(self.engine) as session:
      todo = session.query(Todo).filter_by(id=request.id).one_or_none()
      if not todo:
        logger.info("update todo not found id=\"%s\"", request.id)
        context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                      "todo not found")

      todo.title = request.title
      todo.is_completed = request.is_completed
      session.commit()

    return UpdateTodoResponse()

  def DeleteTodo(self, request, context):
    logger.info("delete todo id=\"%s\"", request.id)
    with Session(self.engine) as session:
      todo = session.query(Todo).filter_by(id=request.id).one_or_none()
      if not todo:
        logger.info("delete todo not found id=\"%s\"", request.id)
        context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                      "todo not found")

      session.delete(todo)
      session.commit()

    return DeleteTodoResponse()
