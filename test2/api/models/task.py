from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(1024), nullable=False)
    done = relationship('Done', back_populates='task', cascade='delete')


class Done(Base):
    __tablename__ = 'dones'
    id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)

    task = relationship('Task', back_populates='done')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
