from typing import Any

import requests

from src.base_api import BaseApi


class HeadHunterApi(BaseApi):
    """Класс HeadHunterApi для подключения и получения вакансий с сайта HeadHunter."""

    per_page: int

    def __init__(self, per_page: int = 50) -> None:
        """
        Инициализирует экземпляр класса HeadHunterApi.

        :param per_page: Количество вакансий на страницу (по умолчанию 50).
        :type per_page: int
        """

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.per_page = per_page
        self.__params = {"text": "", "page": 0, "per_page": self.per_page}
        self.__vacancies = []

    @property
    def url(self) -> str:
        """
        Возвращает URL для запросов к API HeadHunter.

        :return: URL для запросов.
        :rtype: str
        """
        return self.__url

    @property
    def headers(self) -> dict:
        """
        Возвращает заголовки для запросов к API HeadHunter.

        :return: Словарь заголовков.
        :rtype: dict
        """
        return self.__headers

    @property
    def params(self) -> dict:
        """
        Возвращает параметры запроса к API HeadHunter.

        :return: Словарь параметров.
        :rtype: dict
        """
        return self.__params

    @property
    def vacancies(self) -> list:
        """
        Возвращает список полученных вакансий.

        :return: Список вакансий.
        :rtype: list
        """
        return self.__vacancies

    def api_connect(self) -> Any:
        """
        Публичный метод для подключения к API HeadHunter.

        Вызывает приватный метод __api_connect для выполнения HTTP-запроса.

        :return: JSON-ответ от API.
        :rtype: Any
        """
        return self.__api_connect()

    def __api_connect(self) -> Any:
        """
        Приватный метод для выполнения HTTP-запроса к API HeadHunter.

        :return: JSON-ответ от API.
        :rtype: Any
        :raises requests.exceptions.HTTPError: Если статус ответа не равен 200.
        """
        response = requests.get(
            self.__url, headers=self.__headers, params=self.__params
        )
        if response.status_code != 200:
            error_message = f"Ошибка: {response.status_code}"
            raise requests.exceptions.HTTPError(error_message)
        else:
            return response.json()

    def get_vacancies(self, keyword: str, max_per_page: int = 1) -> Any:
        """
        Получает список вакансий по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий (например, "Python").
        :type keyword: str
        :param max_per_page: Максимальное количество страниц для запроса (по умолчанию 1).
        :type max_per_page: int
        :return: Список вакансий, соответствующих ключевому слову.
        :rtype: list
        """
        self.__params["text"] = keyword
        self.__vacancies.clear()
        while self.__params.get("page") < max_per_page:
            data = self.api_connect()
            vacancies = data.get("items", [])
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies
