import os
import sys
import grpc
import logging
from concurrent import futures
from dotenv import load_dotenv
from sqlalchemy import create_engine

from services.todo import TodoService
from grpc_gen import todo_pb2_grpc

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("root")

load_dotenv(".env.local")

HOST = os.getenv("HOST", "localhost:50051")

logger.info("create database engine")
engine = create_engine(os.getenv("DATABASE_URL"))

if __name__ == "__main__":
  logger.info("initialize grpc server")
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

  logger.info("register services")
  todo_service = TodoService(engine)

  todo_pb2_grpc.add_TodoServicer_to_server(todo_service, server)
  server.add_insecure_port(HOST)
  server.start()
  logger.info("server started on %s", HOST)
  server.wait_for_termination()
