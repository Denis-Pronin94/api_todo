from http import HTTPStatus

import pytest

from test.helpers.client import get_tasks
from test.helpers.schema import GetList
from jsonschema import ValidationError


class TestGetTasks:
    """Сьют - тесты на эндпоинт 'get all tasks'."""

    def test_get_tasks(self):
        """Позитивный тест."""
        response = get_tasks.request()
        assert response.status_code == HTTPStatus.OK
        try:
            GetList.parse_obj(response.json())
        except ValidationError as err:
            AssertionError(err)

    @pytest.mark.parametrize(
        'method',
        [
            'delete',
            'post',
            'patch',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативные тесты - неверный метод."""
        response = get_tasks.request(method=method)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
