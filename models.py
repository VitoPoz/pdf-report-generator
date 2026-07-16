from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    object_name = Column(String(100))
    task_name = Column(String(100))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50))
    responsible = Column(String(100))