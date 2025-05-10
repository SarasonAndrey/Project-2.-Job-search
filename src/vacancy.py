from typing import Any


class Vacancy:
    """Класс Vacancy для работы с вакансиями."""

    name: str
    url: str
    salary_from: int
    salary_to: int
    experience: str
    __slots__ = ("name", "url", "salary_from", "salary_to", "experience")

    def __init__(
        self,
        name: str,
        url: str,
        salary_from: int,
        salary_to: int,
        experience: str = "",
    ) -> None:
        """
        Инициализирует экземпляр класса Vacancy.

        :param name: Название вакансии.
        :type name: str
        :param url: Ссылка на вакансию.
        :type url: str
        :param salary_from: Минимальная зарплата (0, если не указана).
        :type salary_from: int
        :param salary_to: Максимальная зарплата (0, если не указана).
        :type salary_to: int
        :param experience: Требуемый опыт работы (по умолчанию пустая строка).
        :type experience: str
        """
        self.name = self.__verify_str_data(name)
        self.url = self.__verify_str_data(url)
        self.salary_from = self.__verify_int_data(salary_from)
        self.salary_to = self.__verify_int_data(salary_to)
        self.experience = experience

    def __str__(self) -> str:
        """
        Возвращает строковое представление вакансии.

        Формат: название, ссылка, информация о зарплате и опыте работы.

        :return: Строковое представление вакансии.
        :rtype: str
        """
        if self.salary_from == 0 and self.salary_to == 0:
            salary_info = "не указана"
        elif self.salary_from == 0:
            salary_info = f"до {self.salary_to}"
        elif self.salary_to == 0:
            salary_info = f"от {self.salary_from}"
        else:
            salary_info = f"от {self.salary_from} до {self.salary_to}"

        if self.experience:
            experience_info = self.experience
        else:
            experience_info = "не указан"

        vacancy_info = f"{self.name}. Ссылка: {self.url}. Зарплата: {salary_info}. Требуемый опыт: {experience_info}."
        return vacancy_info

    def __lt__(self, other: Any) -> Any:
        """
        Сравнивает текущую вакансию с другой по средней зарплате.

        :param other: Другая вакансия для сравнения.
        :type other: Vacancy
        :return: True, если текущая вакансия имеет меньшую среднюю зарплату.
        :rtype: bool
        :raises TypeError: Если other не является экземпляром класса Vacancy.
        """
        other.__verify_salary_other(other)
        return self.salary_average() < other.salary_average()

    def __le__(self, other: Any) -> Any:
        """
        Проверяет, меньше или равна ли текущая вакансия другой по средней зарплате.

        :param other: Другая вакансия для сравнения.
        :type other: Vacancy
        :return: True, если текущая вакансия имеет меньшую или равную среднюю зарплату.
        :rtype: bool
        :raises TypeError: Если other не является экземпляром класса Vacancy.
        """
        other.__verify_salary_other(other)
        return self.salary_average() <= other.salary_average()

    def __gt__(self, other: Any) -> Any:
        """
        Сравнивает текущую вакансию с другой по средней зарплате.

        :param other: Другая вакансия для сравнения.
        :type other: Vacancy
        :return: True, если текущая вакансия имеет большую среднюю зарплату.
        :rtype: bool
        :raises TypeError: Если other не является экземпляром класса Vacancy.
        """
        other.__verify_salary_other(other)
        return self.salary_average() > other.salary_average()

    def __ge__(self, other: Any) -> Any:
        """
        Проверяет, больше или равна ли текущая вакансия другой по средней зарплате.

        :param other: Другая вакансия для сравнения.
        :type other: Vacancy
        :return: True, если текущая вакансия имеет большую или равную среднюю зарплату.
        :rtype: bool
        :raises TypeError: Если other не является экземпляром класса Vacancy.
        """
        other.__verify_salary_other(other)
        return self.salary_average() >= other.salary_average()

    def salary_average(self) -> float:
        """
        Вычисляет среднюю зарплату для вакансии.

        :return: Средняя зарплата (или 0, если данные отсутствуют).
        :rtype: float
        """
        if self.salary_from and self.salary_to:
            return round((self.salary_from + self.salary_to) / 2, 2)
        elif self.salary_from:
            return self.salary_from
        elif self.salary_to:
            return self.salary_to
        else:
            return 0

    @classmethod
    def process_vacancy(cls, vacancy_json_data: dict) -> Any:
        """
        Создает объект Vacancy из JSON-данных.

        :param vacancy_json_data: Словарь с данными о вакансии.
        :type vacancy_json_data: dict
        :return: Экземпляр класса Vacancy.
        :rtype: Vacancy
        """
        name = vacancy_json_data.get("name", "")
        url = vacancy_json_data.get("alternate_url", "")

        salary_info = vacancy_json_data.get("salary", {})
        if salary_info:
            salary_from = salary_info.get("from", 0)
            salary_to = salary_info.get("to", 0)
        else:
            salary_from = 0
            salary_to = 0

        experience_info = vacancy_json_data.get("experience", {})
        if experience_info:
            experience_name = experience_info.get("name", "")
        else:
            experience_name = ""

        return cls(
            name=name,
            url=url,
            salary_from=salary_from,
            salary_to=salary_to,
            experience=experience_name,
        )

    @classmethod
    def cast_to_object_list(cls, vacancy_json_data: list[dict]) -> list:
        """
        Преобразует список JSON-данных в список объектов Vacancy.

        :param vacancy_json_data: Список словарей с данными о вакансиях.
        :type vacancy_json_data: list[dict]
        :return: Список экземпляров класса Vacancy.
        :rtype: list[Vacancy]
        """
        vacancies_list = []
        for vacancy in vacancy_json_data:
            vacancies_list.append(cls.process_vacancy(vacancy))
        return vacancies_list

    def transform_to_dict(self) -> dict:
        """
        Преобразует объект Vacancy в словарь.

        :return: Словарь с данными о вакансии.
        :rtype: dict
        """
        return {
            "name": self.name,
            "alternate_url": self.url,
            "salary": {"from": self.salary_from, "to": self.salary_to},
            "experience": {"name": self.experience},
        }

    @staticmethod
    def __verify_str_data(check_str_data: str) -> str:
        """
        Проверяет, что данные являются строкой.

        :param check_str_data: Данные для проверки.
        :type check_str_data: str
        :return: Проверенные данные.
        :rtype: str
        :raises TypeError: Если данные не являются строкой.
        """
        if not isinstance(check_str_data, str):
            raise TypeError(f"Атрибут {check_str_data} должен быть строкового типа")
        return check_str_data

    @staticmethod
    def __verify_int_data(check_int_data: int) -> int:
        """
        Проверяет, что данные являются целым числом и не отрицательны.

        :param check_int_data: Данные для проверки.
        :type check_int_data: int
        :return: Проверенные данные.
        :rtype: int
        :raises TypeError: Если данные не являются числом.
        :raises ValueError: Если данные отрицательны.
        """
        if check_int_data is None:
            return 0
        if not isinstance(check_int_data, int):
            raise TypeError(f"Атрибут {check_int_data} не является числом")
        if check_int_data < 0:
            raise ValueError(f"Атрибут {check_int_data} не может быть ниже 0")
        return check_int_data

    @staticmethod
    def __verify_salary_other(other_data: Any) -> None:
        """
        Проверяет, что данные относятся к классу Vacancy.

        :param other_data: Данные для проверки.
        :type other_data: Any
        :raises TypeError: Если данные не являются экземпляром класса Vacancy.
        """
        if not isinstance(other_data, Vacancy):
            raise TypeError("Атрибут не относится к классу Vacancy")
