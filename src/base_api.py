from abc import ABC, abstractmethod
from typing import Any


class BaseApi(ABC):
    """Абстрактный класс BaseApi"""

    @abstractmethod
    def api_connect(self) -> dict[Any, Any]:
        """
        Устанавливает соединение с API и возвращает данные.

        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> dict[Any, Any]:
        """
        Получает список вакансий по заданному ключевому слову.

        """
        pass
