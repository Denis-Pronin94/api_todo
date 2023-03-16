from flask import Flask, request

from models import TasksDB

from peewee import DataError

from pydantic import ValidationError

from schema import CreateNewTask, UpdateTask

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/tasks/', methods=['PUT'])
def create_new_task() -> [list, int]:
    """Эндпоинт создания таски."""
    try:
        task = CreateNewTask.parse_obj(request.json)
        values = TasksDB.create(title=task.name, status=1)
        return list(TasksDB.select().where(TasksDB.id == values.id).dicts()), 201
    except ValidationError:
        return 'Ошибка в ключе.', 400
    except DataError:
        return 'Слишком длинное значение ключа. Ключ может быть максимум 250 символов.', 400


@app.route('/tasks', methods=['GET'])
def get_all_task() -> [list, int]:
    """Эндпоинт получения всех тасок."""
    return list(TasksDB.select().dicts()), 200


@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task_status(task_id: int) -> [list, int]:
    """Эндпоинт обнвления статуса таски."""
    try:
        new_status = UpdateTask.parse_obj(request.json)
        valid_status = [1, 2, 3, 4]
        result_status = valid_status.count(new_status.status)
        if result_status > 0:
            list_id = list(TasksDB.select(TasksDB.id).dicts())
            value_task_id = {'id': task_id}
            result = list_id.count(value_task_id)
            if result > 0:
                d = TasksDB.update(status=new_status.status).where(TasksDB.id == task_id)
                d.execute()
                return list(TasksDB.select().where(TasksDB.id == task_id).dicts()), 200
            else:
                return {'error': 'task with id=' + str(task_id) + ' does not exist'}, 400
        else:
            return {'error': 'wrong status'}, 400
    except ValidationError:
        return 'Некорректное значение ключа.', 400


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int) -> [list, int]:
    """Эндпоинт удаления таски."""
    list_id = list(TasksDB.select(TasksDB.id).dicts())
    value_task_id = {'id': task_id}
    result = list_id.count(value_task_id)
    if result > 0:
        delete = TasksDB.delete().where(TasksDB.id == task_id)
        delete.execute()
        return '', 204
    else:
        return {'error': 'task with id=' + str(task_id) + ' does not exist'}, 400


if __name__ == '__main__':
    app.run(debug=True)
