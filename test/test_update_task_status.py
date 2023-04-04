from http import HTTPStatus

import pytest

from app.enums import TaskStatus
from test.helpers.client import update_task_status, create_new_task
from test.helpers.schema import GetList
from jsonschema import ValidationError


class TestUpdateTaskStatus:
    """Сьют - тесты на эндпоинт 'update task status'."""

    @pytest.fixture()
    def get_task_id(self) -> int:
        """Получение task_id."""
        response = create_new_task.request(payload={'name': 'Iron Man'})
        return response.json()['data'][0]['id']

    @pytest.mark.parametrize(
        'payload',
        [
            {'status': TaskStatus.IN_PROGRESS.value},
            {'status': TaskStatus.DONE.value},
            {'status': TaskStatus.CANCELLED.value},
            {'status': TaskStatus.NEW.value},
        ],
    )
    def test_positive(self, get_task_id: int, payload: dict):
        """Позитивные тесты."""
        response = update_task_status.request(
            task_id=get_task_id,
            payload=payload,
        )

        assert response.status_code == HTTPStatus.OK
        try:
            GetList.parse_obj(response.json())
        except ValidationError as err:
            ValueError(err)

    @pytest.fixture
    def payload_positive(self) -> dict:
        return {'status': 2}

    @pytest.mark.parametrize(
        'method',
        [
            'put',
            'get',
            'patch',
        ],
    )
    def test_wrong_method(self, get_task_id: int, method: str, payload_positive: dict):
        """Негатиынве тесты - неправильный метод."""
        response = update_task_status.request(
            method=method,
            task_id=get_task_id,
            payload=payload_positive,
        )

        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    @pytest.mark.parametrize(
        'payload',
        [
            {'status': 5},
            {'status': '5'},
            {'status': 'Iron man'},
            {'status': -4},
            {'status': 0},
            {'sttus': 3},
            {'3': 3},
            {'status': '!@#$%&^*'},
            'status',
            2,
        ],
    )
    def test_wrong_payload(self, get_task_id: int, payload: dict):
        """Негативные тесты - неправильный payload."""
        response = update_task_status.request(
            task_id=get_task_id,
            payload=payload,
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
