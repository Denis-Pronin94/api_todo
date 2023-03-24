from http import HTTPStatus

from flask import Flask, request

from app.enums import TaskStatus
from models import TasksDB

from peewee import DataError

from pydantic import ValidationError

from app.schema import CreateNewTask, UpdateTask, Response

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/tasks/', methods=['PUT'])
def create_new_task() -> [list, int]:
    """Эндпоинт создания таски."""
    try:
        task = CreateNewTask.parse_obj(request.json)
        values = TasksDB.create(title=task.name, status=TaskStatus.NEW.value)
        return Response(
            data=[dict(
                id=values.id,
                title=values.title,
                status=values.status,
                updated_at=values.updated_at
            )]).dict(), HTTPStatus.CREATED
    except ValidationError as e:
        return Response(data=None, error=str(e)).dict(), HTTPStatus.BAD_REQUEST
    except DataError as err:
        return Response(data=None, error=str(err)).dict(), HTTPStatus.BAD_REQUEST


@app.route('/tasks', methods=['GET'])
def get_all_task() -> [list, int]:
    """Эндпоинт получения всех тасок."""
    return Response(data=list(TasksDB.select().dicts())).dict(), HTTPStatus.OK


@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task_status(task_id: int) -> [list, int]:
    """Эндпоинт обнвления статуса таски."""
    try:
        new_status = UpdateTask.parse_obj(request.json)
        valid_status = [1, 2, 3, 4]
        result_status = new_status.status in valid_status
        if result_status:
            list_id = TasksDB.select(TasksDB.id).where(TasksDB.id == task_id)
            if list_id.exists():
                update = TasksDB.update(status=new_status.status).where(TasksDB.id == task_id)
                update.execute()
                return Response(data=list(TasksDB.select().where(TasksDB.id == task_id).dicts())).dict(), HTTPStatus.OK
            else:
                return Response(
                    data=None,
                    error=str(f'{"task with id=" + str(task_id) + " does not exist"}')
                ).dict(), HTTPStatus.BAD_REQUEST
        else:
            return Response(
                error=str
                ('wrong status. Is valid status: 1 - NEW, 2 - IN_PROGRESS, 3 - DONE, 4 - CANCELLED')
            ).dict(), HTTPStatus.BAD_REQUEST
    except ValidationError as err:
        return Response(data=None, error=str(err)).dict(), HTTPStatus.BAD_REQUEST


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int) -> [list, int]:
    """Эндпоинт удаления таски."""
    list_id = list(TasksDB.select(TasksDB.id).dicts())
    value_task_id = {'id': task_id}
    result = list_id.count(value_task_id)
    if result > 0:
        delete = TasksDB.delete().where(TasksDB.id == task_id)
        delete.execute()
        return '', HTTPStatus.NO_CONTENT
    else:
        return Response(
            data=None,
            error=str(f'{"task with id=" + str(task_id) + " does not exist"}')
        ).dict(), HTTPStatus.BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)
