import datetime

from app.config import HOST, DATABASE, PASSWORD, PORT, USER

from peewee import (
    CharField,
    DateTimeField,
    IntegerField,
    Model,
    PostgresqlDatabase,
    PrimaryKeyField,
)

db = PostgresqlDatabase(DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)


class BaseModel(Model):
    """Базовый класс БД."""

    class Meta:
        """Обязательный класс внутри базового класса БД."""

        database = db


class TasksDB(BaseModel):
    """Базовый класс базы данных TasksDB."""

    class Meta:
        """Обязательный класс внутри базового класса БД."""

        db_table = 'tasks'

    id = PrimaryKeyField(primary_key=True)
    title = CharField(null=False)
    status = IntegerField()
    updated_at = DateTimeField(default=datetime.datetime.now)
