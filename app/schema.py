import re
from datetime import datetime
from typing import Union

from pydantic import BaseModel, validator


class CreateNewTask(BaseModel):
    """Schema create new task."""

    name: str

    @validator('name')
    def name_task(cls, v: str) -> str:
        """Валидация name."""
        match = re.match(r'^[a-z, A-Z]\D*', v)
        if match is None:
            raise ValueError(
                'Некорректное Имя. Имя должно содержать только латинские буквы (допускаются пробелы).')
        return v


class UpdateTask(BaseModel):
    """Schema update status task."""

    status: int


class ValuesTasks(BaseModel):
    """Схема массива data."""

    id: int
    status: int
    title: str
    updated_at: datetime


class Response(BaseModel):
    """Схема response."""

    data: Union[list[ValuesTasks], None]
    error: Union[str, None] = None
