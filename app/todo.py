from http import HTTPStatus

from flask import Flask, request

from app.models import TasksDB

from peewee import DataError

from pydantic import ValidationError

from app.schema import CreateNewTask, UpdateTask

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/tasks/', methods=['PUT'])
def create_new_task() -> [list, int]:
    """Эндпоинт создания таски."""
    try:
        task = CreateNewTask.parse_obj(request.json)
        values = TasksDB.create(title=task.name, status=1)
        return dict(
            id=values.id,
            title=values.title,
            status=values.status,
            updated_at=values.updated_at
        ), HTTPStatus.CREATED
    except ValidationError as e:
        return str(e), HTTPStatus.BAD_REQUEST
    except DataError as err:
        return str(err), HTTPStatus.BAD_REQUEST


@app.route('/tasks', methods=['GET'])
def get_all_task() -> [list, int]:
    """Эндпоинт получения всех тасок."""
    return list(TasksDB.select().dicts()), HTTPStatus.OK


@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task_status(task_id: int) -> [list, int]:
    """Эндпоинт обнвления статуса таски."""
    try:
        new_status = UpdateTask.parse_obj(request.json)
        valid_status = [1, 2, 3, 4]
        result_status = valid_status.count(new_status.status)
        if result_status > 0:
            list_id = list(TasksDB.select(TasksDB.id).where(TasksDB.id == task_id).dicts())
            value_task_id = {'id': task_id}
            result = list_id.count(value_task_id)
            if result > 0:
                d = TasksDB.update(status=new_status.status).where(TasksDB.id == task_id)
                d.execute()
                return list(TasksDB.select().where(TasksDB.id == task_id).dicts()), HTTPStatus.OK
            else:
                return {'error': 'task with id=' + str(task_id) + ' does not exist'}, HTTPStatus.BAD_REQUEST
        else:
            return {'error': 'wrong status'}, HTTPStatus.BAD_REQUEST
    except ValidationError as err:
        return str(err), HTTPStatus.BAD_REQUEST


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
        return {'error': 'task with id=' + str(task_id) + ' does not exist'}, HTTPStatus.BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True)
