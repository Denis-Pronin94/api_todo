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
    class Meta:
        table_name = "tasksdb"


def forward(old_orm, new_orm):
    old_tasksdb = old_orm['tasksdb']
    tasksdb = new_orm['tasksdb']
    return [
        # Convert datatype of the field tasksdb.updated_at_date: DATETIME -> BIGINT,
        tasksdb.update({tasksdb.updated_at_date: old_tasksdb.updated_at_date.cast('INTEGER')}).where(old_tasksdb.updated_at_date.is_null(False)),
    ]


def backward(old_orm, new_orm):
    old_tasksdb = old_orm['tasksdb']
    tasksdb = new_orm['tasksdb']
    return [
        # Don't know how to do the conversion correctly, use the naive,
        tasksdb.update({tasksdb.updated_at_date: old_tasksdb.updated_at_date}).where(old_tasksdb.updated_at_date.is_null(False)),
    ]
