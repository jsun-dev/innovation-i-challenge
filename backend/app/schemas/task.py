from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    duration = Column(Integer)
    sqlite_autoincrement=True