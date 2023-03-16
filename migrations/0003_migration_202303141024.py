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
    updated_at_date = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "tasksdb"


def forward(old_orm, new_orm):
    tasksdb = new_orm['tasksdb']
    return [
        # Apply default value datetime.datetime(2023, 3, 14, 10, 24, 43, 700832) to the field tasksdb.updated_at_date,
        tasksdb.update({tasksdb.updated_at_date: datetime.datetime(2023, 3, 14, 10, 24, 43, 700832)}).where(tasksdb.updated_at_date.is_null(True)),
    ]
