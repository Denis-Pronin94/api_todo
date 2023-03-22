from enum import Enum, auto


class TaskStatus(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    CANCELLED = auto()
