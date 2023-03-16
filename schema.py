from pydantic import BaseModel


class CreateNewTask(BaseModel):
    """Schema create new task."""

    name: str


class UpdateTask(BaseModel):
    """Schema create new task."""

    status: int
