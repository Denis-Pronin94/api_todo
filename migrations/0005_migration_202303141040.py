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
    updated_at_date = TimestampField(default=datetime.datetime.now)
    date_updated_at_date = TimestampField(default=datetime.datetime.now)
    class Meta:
        table_name = "tasksdb"


def forward(old_orm, new_orm):
    tasksdb = new_orm['tasksdb']
    return [
        # Apply default value datetime.datetime(2023, 3, 14, 10, 40, 14, 455586) to the field tasksdb.date_updated_at_date,
        tasksdb.update({tasksdb.date_updated_at_date: datetime.datetime(2023, 3, 14, 10, 40, 14, 455586)}).where(tasksdb.date_updated_at_date.is_null(True)),
    ]
