from abc import ABC, abstractmethod
from typing import Any


class BaseApi(ABC):
    """Абстрактный класс BaseApi"""

    @abstractmethod
    def api_connect(self) -> dict[Any, Any]:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> dict[Any, Any]:
        pass
