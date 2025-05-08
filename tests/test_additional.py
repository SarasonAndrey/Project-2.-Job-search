from typing import Any

import pytest

from src.additional import get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def test_get_top_vacancies_all(vacancies_list: list[Vacancy], top_n: int = 0) -> None:
    assert len(vacancies_list) == 3
    assert vacancies_list[0].salary_from == 10
    assert vacancies_list[0].salary_to == 20
    top_vacancies = get_top_vacancies(vacancies_list)
    assert len(top_vacancies) == 3
    assert top_vacancies[0].salary_from == 50
    assert top_vacancies[0].salary_to == 70


def test_get_top_vacancies_two(vacancies_list: list[Vacancy], top_n: int = 0) -> None:
    top_n = 2
    assert len(vacancies_list) == 3
    assert vacancies_list[0].salary_from == 10
    assert vacancies_list[0].salary_to == 20
    top_vacancies = get_top_vacancies(vacancies_list, top_n)
    assert len(top_vacancies) == 2
    assert top_vacancies[1].salary_from == 10
    assert top_vacancies[1].salary_to == 20


def test_get_top_vacancies_error(vacancies_list: list[Vacancy], top_n: int = 0) -> None:
    top_n = 5
    with pytest.raises(ValueError, match="В списке нет нужного кол-ва вакансий"):
        get_top_vacancies(vacancies_list, top_n)


def test_print_vacancies(capsys: Any, vacancies_list_from_file: list[Vacancy]) -> None:
    print_vacancies(vacancies_list_from_file)
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == "Python Developer. Ссылка: <https://hh.ru/vacancy/123456>. Зарплата: от 10 до 20. "
               "Требуемый опыт: Требования: опыт работы от 3 лет."
    )


def test_print_vacancies_empty(capsys: Any) -> None:
    empty_list: list = []
    print_vacancies(empty_list)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""
