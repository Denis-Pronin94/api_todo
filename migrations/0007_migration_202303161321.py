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
    date_updated_at_date = TimestampField(default=datetime.datetime.now)
    date = TimestampField(default=datetime.datetime.now)
    class Meta:
        table_name = "tasksdb"


def forward(old_orm, new_orm):
    tasksdb = new_orm['tasksdb']
    return [
        # Apply default value datetime.datetime(2023, 3, 16, 13, 21, 31, 458277) to the field tasksdb.date,
        tasksdb.update({tasksdb.date: datetime.datetime(2023, 3, 16, 13, 21, 31, 458277)}).where(tasksdb.date.is_null(True)),
    ]
