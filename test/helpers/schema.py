from typing import Union

from pydantic import BaseModel


class GetTasksSchema(BaseModel):
    """Schema массива data."""

    id: int
    status: int
    title: str
    updated_at: str


class GetList(BaseModel):
    """Schema response."""

    data: Union[list[GetTasksSchema], None]
    error: Union[str, None] = None
