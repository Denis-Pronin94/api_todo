import requests

BASE_URL = 'http://127.0.0.1:5000/tasks'


class BaseClient:
    """Базовый класс для API-клиентов."""

    def __init__(self):
        """Дефолтные url и заголовок."""
        self.base_url = BASE_URL


class GetTasks(BaseClient):
    """Возвращает все таски."""

    def request(self, method: str = 'GET') -> requests.Response:
        """Отправка запроса."""
        return requests.request(method, url=BASE_URL)


class CreateNewTask(BaseClient):
    """Создание новой таски."""
    def request(self, payload: dict, method: str = 'PUT') -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{BASE_URL}/',
            json=payload,
        )


class UpdateTaskStatus(BaseClient):
    """Обновление статуса таски."""
    def request(
            self,
            payload: dict,
            method: str = 'POST',
            task_id: int = None) -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{BASE_URL}/{task_id}',
            json=payload,
        )


class DeleteTask(BaseClient):
    """Удаление таски."""
    def request(self, method: str = 'DELETE', task_id: int = None) -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{BASE_URL}/{task_id}',
        )


delete_task = DeleteTask()
update_task_status = UpdateTaskStatus()
create_new_task = CreateNewTask()
get_tasks = GetTasks()
