from .base import Base
from pydantic.types import PositiveInt

class Task(Base):
    id : int = None
    name : str = None
    description : str = None
    duration : PositiveInt