import pytest

from src.vacancy import Vacancy


def test_vacancy_init(vacancy_instance: Vacancy) -> None:
    """Тест проверяет корректное создания экземпляра класса Vacancy и его атрибутов."""
    assert vacancy_instance.name == "Python Developer"
    assert vacancy_instance.url == "1"
    assert vacancy_instance.salary_from == 10
    assert vacancy_instance.salary_to == 50
    assert vacancy_instance.experience == "Опыт работы от 2 лет"


def test_vacancy_str(vacancy_instance: Vacancy) -> None:
    """Тест проверяет корректный вывод метода str."""
    assert (
        str(vacancy_instance)
        == "Python Developer. Ссылка: 1. Зарплата: от 10 до 50. Требуемый опыт: Опыт работы от 2 лет."
    )


def test_vacancy_str_with_zero() -> None:
    """Тест проверяет корректный вывод метода str, когда значение зарплаты равно 0 и/или опыт работы не указан."""
    vacancy_wo_salary_from = Vacancy("Python", "1", 0, 50, "Опыт")
    assert (
        str(vacancy_wo_salary_from)
        == "Python. Ссылка: 1. Зарплата: до 50. Требуемый опыт: Опыт."
    )
    vacancy_wo_salary_to = Vacancy("Python", "1", 20, 0, "Опыт")
    assert (
        str(vacancy_wo_salary_to)
        == "Python. Ссылка: 1. Зарплата: от 20. Требуемый опыт: Опыт."
    )
    vacancy_wo_salary = Vacancy("Python", "1", 0, 0, "Опыт")
    assert (
        str(vacancy_wo_salary)
        == "Python. Ссылка: 1. Зарплата: не указана. Требуемый опыт: Опыт."
    )
    vacancy_wo_experience = Vacancy("Python", "1", 0, 0, "")
    assert (
        str(vacancy_wo_experience)
        == "Python. Ссылка: 1. Зарплата: не указана. Требуемый опыт: не указан."
    )


def test_vacancies_math_comparison(
    vacancy_instance: Vacancy, vacancy_instance_other: Vacancy
) -> None:
    """Тест проверяет корректное сравнение вакансий по средней зарплате методами <, <=, >, >=."""
    check_lt = vacancy_instance < vacancy_instance_other
    assert check_lt
    check_le = vacancy_instance <= vacancy_instance_other
    assert check_le
    check_gt = vacancy_instance > vacancy_instance_other
    assert not check_gt
    check_ge = vacancy_instance >= vacancy_instance_other
    assert not check_ge


def test_salary_average(vacancy_instance: Vacancy) -> None:
    """Тест проверяет корректный вывод средней зарплаты."""
    assert vacancy_instance.salary_average() == 30
    Vacancy("Python Developer", "1", 10, 50, "Опыт работы от 2 лет")


def test_salary_average_with_zero(vacancy_instance: Vacancy) -> None:
    """Тест проверяет корректный вывод средней зарплаты, когда одно из значений или все значения зарплаты равны 0."""
    vacancy_wo_salary_from = Vacancy("Python", "1", 0, 50, "Опыт")
    assert vacancy_wo_salary_from.salary_average() == 50
    vacancy_wo_salary_to = Vacancy("Python", "1", 20, 0, "Опыт")
    assert vacancy_wo_salary_to.salary_average() == 20
    vacancy_wo_salary = Vacancy("Python", "1", 0, 0, "Опыт")
    assert vacancy_wo_salary.salary_average() == 0


def test_process_vacancy() -> None:
    """Тест проверяет корректную обработку словаря с вакансией и возвращает экземпляр класса Vacancy."""
    test_vacancy = {
        "name": "Python",
        "alternate_url": "12",
        "salary": {"from": 100, "to": 150},
        "experience": {"name": "опыт"},
    }
    process_vacancy = Vacancy.process_vacancy(test_vacancy)
    assert process_vacancy.name == "Python"
    assert process_vacancy.url == "12"
    assert process_vacancy.salary_from == 100
    assert process_vacancy.salary_to == 150
    assert process_vacancy.experience == "опыт"


def test_process_vacancy_with_empty() -> None:
    """Тест проверяет корректную обработку словаря с вакансией, когда не найдены/переданы данные о зарплате и/или
    опыте работы."""
    test_vacancy = {
        "name": "Python",
        "alternate_url": "12",
        "salary": {},
        "experience": {},
    }
    process_vacancy = Vacancy.process_vacancy(test_vacancy)
    assert process_vacancy.salary_from == 0
    assert process_vacancy.salary_to == 0
    assert process_vacancy.experience == ""


def test_cast_to_object_list() -> None:
    """Тест проверяет корректную работу метода по конвертации json-данных в список экземпляров класса."""
    test_vacancy = [
        {
            "name": "Java",
            "alternate_url": "123",
            "salary": {"from": 30, "to": 35},
            "experience": {"name": "Опыт"},
        }
    ]
    vacancy_cast_to_object = Vacancy.cast_to_object_list(test_vacancy)
    for vacancy in vacancy_cast_to_object:
        assert vacancy.name == "Java"
        assert vacancy.url == "123"
        assert vacancy.salary_from == 30
        assert vacancy.salary_to == 35
        assert vacancy.experience == "Опыт"


def test_transform_to_dict(vacancy_instance: Vacancy) -> None:
    """Тест проверяет корректное преобразование экземпляра класса в словарь."""
    assert vacancy_instance.transform_to_dict() == {
        "name": "Python Developer",
        "alternate_url": "1",
        "salary": {"from": 10, "to": 50},
        "experience": {"name": "Опыт работы от 2 лет"},
    }


def test_verify_data_incorrect() -> None:
    """Тест проверяет работу валидации, когда переданы некорректные данные."""

    with pytest.raises(TypeError, match="Атрибут 22 должен быть строкового типа"):
        Vacancy(22, "1", 10, 50, "Опыт работы от 2 лет")

    with pytest.raises(TypeError, match="Атрибут 10 не является числом"):
        Vacancy("Python", "1", "10", 50, "Опыт работы от 2 лет")

    with pytest.raises(ValueError, match="Атрибут -5 не может быть ниже 0"):
        Vacancy("Python", "1", -5, 50, "Опыт работы от 2 лет")
