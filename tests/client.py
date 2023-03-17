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


get_tasks = GetTasks()
