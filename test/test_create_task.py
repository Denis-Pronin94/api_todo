from http import HTTPStatus

import pytest

from test.helpers.client import create_new_task
from test.helpers.schema import GetList
from jsonschema import ValidationError


class TestCreateTask:
    """Сьют - тесты на эндпоинт 'create new task'."""

    @pytest.mark.parametrize(
        'payload',
        [
            {'name': 'Man'},
            {'name': 'man'},
            {'name': 'iron man'},
            {'name': 'IRON MAN'},
            {'name': 'Iron man'},
            {'name': 'Iron Man'},
            {'name': 'I'},
            {'name': 'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man '
                     'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man '
                     'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iro'},
        ]
    )
    def test_positive(self, payload: dict):
        """Позитивные тесты."""
        response = create_new_task.request(payload)

        assert response.status_code == HTTPStatus.CREATED
        try:
            GetList.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.fixture
    def payload_positive(self) -> dict:
        return {'name': 'Iron man'}

    @pytest.mark.parametrize(
        'method',
        [
            'post',
            'get',
            'delete',
            'patch',
        ],
    )
    def test_wrong_method(self, payload_positive: dict, method: str):
        """Негативные тесты - неправильный метод."""
        response = create_new_task.request(
            method=method,
            payload=payload_positive,
        )

        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    @pytest.mark.parametrize(
        'payload',
        [
            {},
            {'name': ''},
            {'ame': 'Iron man'},
            {'Iron man': 'Iron man'},
            {123: 'Iron man'},
            {'Name': 'Iron man'},
            [
                {'name': 'Iron man'},
                {'name': 'Capitan America'}
            ],
            ['name', 'Capitan America'],
            ['name'],
            ('name', 'Capitan America'),
            'name',
            123,
            {'name': '123'},
            {'name': 'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man '
                     'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man '
                     'Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron man Iron'},
        ],
    )
    def test_wrong_payload(self, payload: dict):
        """Негативные тесты - неправильный payload."""
        response = create_new_task.request(payload=payload)

        assert response.status_code == HTTPStatus.BAD_REQUEST
