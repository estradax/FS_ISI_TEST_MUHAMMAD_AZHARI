from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Todo(Base):
  __tablename__ = "todo"

  id = Column(String, primary_key=True)
  title = Column(String, nullable=False)
  is_completed = Column(Boolean, nullable=False, default=False)
  created_at = Column(DateTime(timezone=True),
                      nullable=False, default=func.now())
  updated_at = Column(DateTime(timezone=True),
                      nullable=False, default=func.now(), onupdate=func.now())

  def __repr__(self):
    return f"Todo(id={self.id!r}, title={self.title!r}, is_completed={self.is_completed!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
