from http import HTTPStatus

from client import get_tasks


class TestGetTasks:

    def test_get_tasks(self):
        response = get_tasks.request()
        assert response.status_code == HTTPStatus.OK

