import json
from pathlib import Path
from typing import Any

from src.base_files import BaseFiles

BASEDIR = Path(__file__).resolve().parent.parent


class JsonSaver(BaseFiles):
    """Класс JsonSaver для получения данных из файла, удаления и добавления данных."""

    file_path: str

    def __init__(self, file_path: str = "data") -> None:
        """
        Инициализирует экземпляр класса JsonSaver.

        :param file_path: Имя файла (без расширения), в котором хранятся данные (по умолчанию "data").
        :type file_path: str
        """
        self.__file_path = Path(BASEDIR / "data" / file_path)

    @property
    def file_path(self) -> Path:
        """
        Возвращает путь к JSON-файлу.

        :return: Путь к файлу в виде объекта Path.
        :rtype: Path
        """
        return self.__file_path

    def get_data_from_file(self) -> Any:
        """
        Читает данные из JSON-файла.

        Если файл не существует или содержит некорректные данные, возвращает пустой список.

        :return: Список данных из JSON-файла.
        :rtype: list
        """
        try:
            with open(f"{self.__file_path}.json", "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def add_data_to_file(self, data: Any) -> None:
        """
        Добавляет новые данные в JSON-файл.

        Если данные уже существуют в файле, они не будут добавлены повторно.

        :param data: Данные, которые нужно добавить в файл (обычно словарь или список).
        :type data: Any
        """
        json_file_data = self.get_data_from_file()
        if data not in json_file_data:
            json_file_data.append(data)

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)

    def delete_data_from_file(self, data: Any) -> None:
        """
        Удаляет данные из JSON-файла.

        Если данные не найдены в файле, выводится сообщение об ошибке.

        :param data: Данные, которые нужно удалить из файла.
        :type data: Any
        """
        json_file_data = self.get_data_from_file()
        try:
            json_file_data.remove(data)
        except ValueError:
            print("Данные не найдены")

        with open(f"{self.__file_path}.json", "w", encoding="utf-8") as json_file:
            json.dump(json_file_data, json_file, indent=4, ensure_ascii=False)
