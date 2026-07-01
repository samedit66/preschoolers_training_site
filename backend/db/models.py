from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, func, JSON

from backend.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum("admin", "user", name="user_roles"), default="user")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon_url = Column(String)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    type = Column(String, default="choice", nullable=False)
    question = Column(String, nullable=False)
    options = Column(JSON, nullable=False)
    correct_answer = Column(String, nullable=False)
    image = Column(String, nullable=True)
    difficulty_level = Column(Integer, default=1)
    min_age = Column(Integer, default=2)
    max_age = Column(Integer, default=5)


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    is_correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
