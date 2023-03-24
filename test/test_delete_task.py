from http import HTTPStatus

import pytest

from test.helpers.client import delete_task, create_new_task
from test.helpers.schema import GetList
from jsonschema import ValidationError


class TestDeleteTask:
    """Сьют - тесты на эндпоинт 'delete task'."""
    @pytest.fixture
    def get_task_id(self) -> int:
        """Получение task_id."""
        response = create_new_task.request(payload={'name': 'Iron Man'})
        return response.json()['data'][0]['id']

    def test_positive(self, get_task_id: int):
        """Позитивные тесты."""
        response = delete_task.request(task_id=get_task_id)

        assert response.status_code == HTTPStatus.NO_CONTENT

    @pytest.mark.parametrize(
        'method',
        [
            'get',
            'put',
            'patch',
        ],
    )
    def test_wrong_status(self, method: str, get_task_id: int):
        """Негатиынве тесты - неправильный метод."""
        response = delete_task.request(
            method,
            task_id=get_task_id,
        )

        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    def test_wrong_task_id(self, get_task_id: int):
        """Негатиынве тесты - несуществущий task_id."""
        response_delete_task = delete_task.request(task_id=get_task_id)

        assert response_delete_task.status_code == HTTPStatus.NO_CONTENT

        response = delete_task.request(task_id=get_task_id)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        try:
            GetList.parse_obj(response.json())
        except ValidationError as err:
            ValueError(err)

    @pytest.mark.parametrize(
        'task_id',
        [
            'man',
            '/iron_man',
            '!@#$%^&*(',
            {'status': 2},
            ['name'],
        ],
    )
    def test_wrong_value_task_id(self, task_id: str):
        """Негатиынве тесты - неправильный task_id."""
        response = delete_task.request(task_id=task_id)

        assert response.status_code == HTTPStatus.NOT_FOUND
