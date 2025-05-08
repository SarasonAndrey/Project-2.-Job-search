import json
from pathlib import Path
from typing import Any

from src.base_files import BaseFiles

BASEDIR = Path(__file__).resolve().parent.parent


class JsonSaver(BaseFiles):
    """Класс JsonSaver предназначен для получения данных из файла, удаления и добавления данных."""

    file_path: str

    def __init__(self, file_path: str = "data") -> None:
        """Метод для инициализации экземпляра класса JsonSaver."""

        self.__file_path = Path(BASEDIR / "data" / file_path)

    @property
    def file_path(self) -> Path:
        """Геттер возвращает путь к файлу, в который сохраняются данные в json-формате."""
        return self.__file_path

    def get_data_from_file(self) -> Any:
        """Метод для получения данных из файла. Используется для вывода, добавления и удаления данных из файла."""
        try:
            with open(f"{self.__file_path}.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def add_data_to_file(self, data: Any) -> None:
        """Метод для добавления данных в файл."""
        json_file_data = self.get_data_from_file()
        if data not in json_file_data:
            json_file_data.append(data)

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)

    def delete_data_from_file(self, data: Any) -> None:
        """Метод для удаления данных из файла."""
        json_file_data = self.get_data_from_file()
        try:
            json_file_data.remove(data)
        except ValueError:
            print("Данные не найдены")

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)
