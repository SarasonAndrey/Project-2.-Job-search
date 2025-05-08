from abc import ABC, abstractmethod


class BaseFiles(ABC):
    """Абстрактный класс BaseFiles. В нем реализованы класс-методы для получения данных из файла, добавления данных
    в файл и удаления данных из файла."""

    @abstractmethod
    def get_data_from_file(self) -> list:
        """Абстрактный метод для получения данных из файла."""
        pass

    @abstractmethod
    def add_data_to_file(self, data: dict) -> None:
        """Абстрактный метод для добавления данных в файл."""
        pass

    @abstractmethod
    def delete_data_from_file(self, data: dict) -> None:
        """Абстрактный метод для удаления данных из файла."""
        pass
