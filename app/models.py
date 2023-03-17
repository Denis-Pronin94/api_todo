import datetime

from app.config import HOST, NAME, PASSWORD, PORT, USER

from peewee import (
    CharField,
    DateTimeField,
    IntegerField,
    Model,
    PostgresqlDatabase,
    PrimaryKeyField,
)

db = PostgresqlDatabase(NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)


class BaseModel(Model):
    """Базовый класс БД."""

    class Meta:
        """Обязательный класс внутри базового класса БД."""

        database = db


class TasksDB(BaseModel):
    """Базовый класс базы данных TasksDB."""

    class Meta:
        """Обязательный класс внутри базового класса БД."""

        da_table = 'tasks'

    id = PrimaryKeyField(primary_key=True)
    title = CharField()
    status = IntegerField()
    updated_at = DateTimeField(default=datetime.datetime.now)
