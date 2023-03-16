# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class TasksDB(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    title = CharField(max_length=255)
    status = IntegerField()
    updated_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "tasksdb"


def backward(old_orm, new_orm):
    tasksdb = new_orm['tasksdb']
    return [
        # Apply default value datetime.datetime(2023, 3, 16, 13, 30, 38, 357840) to the field tasksdb.date_updated_at_date,
        tasksdb.update({tasksdb.date_updated_at_date: datetime.datetime(2023, 3, 16, 13, 30, 38, 357840)}).where(tasksdb.date_updated_at_date.is_null(True)),
    ]
