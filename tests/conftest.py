import pytest

from src.head_hunter_api import HeadHunterApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


@pytest.fixture
def vacancies_list() -> list[Vacancy]:
    return [
        Vacancy(
            "Python Developer",
            "<https://hh.ru/vacancy/123456>",
            10,
            20,
            "Требования: опыт работы от 3 лет...",
        ),
        Vacancy(
            "Java Developer",
            "<https://hh.ru/vacancy/123457>",
            0,
            15,
            "Требования: опыт работы от 3 лет...",
        ),
        Vacancy(
            "Python Developer",
            "<https://hh.ru/vacancy/123458>",
            50,
            70,
            "Требования: опыт работы от 3 лет...",
        ),
    ]


@pytest.fixture
def vacancies_list_from_file() -> list:
    return [
        Vacancy(
            "Python Developer",
            "<https://hh.ru/vacancy/123456>",
            10,
            20,
            "Требования: опыт работы от 3 лет",
        )
    ]


@pytest.fixture
def vacancy_instance() -> Vacancy:
    return Vacancy("Python Developer", "1", 10, 50, "Опыт работы от 2 лет")


@pytest.fixture
def vacancy_instance_other() -> Vacancy:
    return Vacancy("Java Developer", "2", 100, 120, "Опыт работы от 3 лет")


@pytest.fixture
def head_hunter_init() -> HeadHunterApi:
    return HeadHunterApi()


@pytest.fixture
def api_connect_data() -> list[dict]:
    return [
        {
            "name": "Python Developer",
            "alternate_url": "<https://hh.ru/vacancy/123456>",
            "salary": {"from": 100000, "to": 150000},
            "experience": {"name": "Требования: опыт работы от 3 лет"},
        }
    ]


@pytest.fixture
def api_connect_data_before_sort() -> dict:
    return {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "<https://hh.ru/vacancy/123456>",
                "salary": {"from": 100000, "to": 150000},
                "experience": {"name": "Требования: опыт работы от 3 лет"},
            },
            {
                "items": {
                    "name": "Python Developer",
                    "alternate_url": "<https://hh.ru/vacancy/123458>",
                    "salary": {"from": 300000, "to": 400000},
                    "experience": {"name": "Требования: опыт работы от 5 лет"},
                }
            },
        ]
    }


@pytest.fixture
def json_saver_init() -> JsonSaver:
    return JsonSaver()


@pytest.fixture
def vacancy_dict() -> dict:
    return {"name": "Python Developer"}
