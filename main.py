from src.additional import get_top_vacancies, print_vacancies
from src.head_hunter_api import HeadHunterApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем. В функции проверяются следующие возможности: получение вакансий
    по ключевому запросу на сайте HeadHunter.ru, вывод топ N ваканский по средней зарплате(N задает пользователь),
    добавление и удаление вакансий, сохранение созданных вакансий в файл и вывод их из файла в консоль.
    """
    # input("Введите поисковый запрос: ")
    search_query = "Python Developer"
    # int(input("Введите количество вакансий для вывода в топ N: "))
    top_n = 3

    hh_api = HeadHunterApi()

    hh_vacancies = hh_api.get_vacancies(search_query, 20)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    top_vacancies = get_top_vacancies(vacancies_list, top_n)
    print("Отсортированные вакансии по средней зарплате:")
    print_vacancies(top_vacancies)

    new_vacancy = Vacancy(
        "Python",
        "<https://hh.ru/vacancy/123456>",
        100,
        150,
        "Требования: опыт работы от 3 лет",
    )
    new_vacancy_to_delete = Vacancy(
        "Java", "<https://hh.ru/vacancy/123457>", 120, 150, "Требования: ..."
    )

    json_saver = JsonSaver()

    new_vacancy_to_dict = Vacancy.transform_to_dict(new_vacancy)
    vacancy_to_dict = Vacancy.transform_to_dict(new_vacancy_to_delete)

    json_saver.add_data_to_file(new_vacancy_to_dict)
    json_saver.add_data_to_file(vacancy_to_dict)

    vacancy_from_file = json_saver.get_data_from_file()

    json_saver.delete_data_from_file(vacancy_to_dict)

    vacancy_from_file_list = Vacancy.cast_to_object_list(vacancy_from_file)

    print("Список вакансий из файла:")
    print_vacancies(vacancy_from_file_list)


if __name__ == "__main__":
    user_interaction()
