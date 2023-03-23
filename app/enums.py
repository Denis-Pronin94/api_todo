from enum import Enum, auto


class TaskStatus(Enum):
    """Статусы."""

    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    CANCELLED = auto()
