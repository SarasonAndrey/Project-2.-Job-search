from abc import ABC, abstractmethod


class BaseFiles(ABC):
    """Абстрактный класс BaseFiles"""

    @abstractmethod
    def get_data_from_file(self) -> list:
        """Читает данные из файла и возвращает их в виде списка словарей."""
        pass

    @abstractmethod
    def add_data_to_file(self, data: dict) -> None:
        """Добавляет новые данные в файл."""
        pass

    @abstractmethod
    def delete_data_from_file(self, data: dict) -> None:
        """Удаляет данные из файла."""
        pass
