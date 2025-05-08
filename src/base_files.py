from abc import ABC, abstractmethod


class BaseFiles(ABC):
    """Абстрактный класс BaseFiles"""

    @abstractmethod
    def get_data_from_file(self) -> list:
        pass

    @abstractmethod
    def add_data_to_file(self, data: dict) -> None:
        pass

    @abstractmethod
    def delete_data_from_file(self, data: dict) -> None:
        pass
