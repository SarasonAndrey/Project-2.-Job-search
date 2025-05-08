from src.vacancy import Vacancy


def get_top_vacancies(vacancies_list: list[Vacancy], top_n: int = 0) -> list[Vacancy]:
    """Функция возвращает осортированный список вакансий"""
    sorted_list = sorted(vacancies_list, reverse=True)
    if len(vacancies_list) < top_n:
        raise ValueError("В списке нет нужного кол-ва вакансий")
    if top_n:
        return sorted_list[:top_n]
    else:
        return sorted_list


def print_vacancies(vacancies_list: list[Vacancy]) -> None:
    for vacancy in vacancies_list:
        print(vacancy)
