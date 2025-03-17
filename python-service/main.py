import os
import grpc
from concurrent import futures
from dotenv import load_dotenv
from sqlalchemy import create_engine

from grpc_gen import todo_pb2_grpc
from grpc_gen.todo_pb2_grpc import TodoServicer

load_dotenv(".env.local")

engine = create_engine(os.getenv("DATABASE_URL"))

class TodoService(TodoServicer):
  def GetTodos(self, request, context):
    return super().GetTodos(request, context)

if __name__ == "__main__":
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
  server.add_insecure_port("[::]:" + "50051")
  server.start()
  print("Server started, listening on " + "50051")
  server.wait_for_termination()
