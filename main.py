from src.utils import user_communication

from src.classes.api_vacancy_handlers.hh_vacancy_api import HHVacancyAPI
from src.classes.api_vacancy_handlers.super_job_vacancy_api import SJVacancyAPI

from src.classes.vacancy import Vacancy

from src.classes.file_data_managers.json_favorites_vacancies import JSONFavoritesVacancies
from src.classes.file_data_managers.json_data_manager import JSONVacancyStorage


def main():
    # Выводится приветствие.
    user_communication.print_greeting()

    # Запускается бесконечный цикл, пока пользователь не прервет работу программы.
    while True:
        # Создается список экземпляров вакансий, полученных из ответов API.
        # Платформы для сбора вакансий предлагается выбрать пользователю.
        vacancies = get_vacancies_from_api()

        # Если список с вакансиями пустой, предлагается повторить запрос.
        # Если пользователь отказывается, программа завершается и выводится прощание.
        if user_communication.check_list_completeness(vacancies) is False:
            if user_communication.suggest_to_continue():
                continue
            else:
                user_communication.print_goodbye()
                break

        # Предлагается отсортировать вакансии по зарплате от большей к меньшей.
        if user_communication.sort_vacancies():
            sorted_vacancies = sorted(vacancies, reverse=True)
            vacancies = sorted_vacancies

        # Выводятся строковые представления экземпляров вакансий.
        for vacancy in vacancies:
            print(vacancy)

        # Выводится информация о сохранении вакансий в json файле.
        # И предлагается добавить понравившиеся вакансии в избранное в формате json.
        json_manipulator(vacancies)

        # В конце цикла предлагается ввести запросы еще раз для поиска других вакансий.
        # Если пользователь отказывается, программа завершается и выводится прощание.
        if user_communication.suggest_to_continue():
            continue

        else:
            user_communication.print_goodbye()
            break


def get_vacancies_from_api():
    """
    Возвращает список экземпляров вакансий, полученных из ответов API.
    Списки создаются в зависимости от выбора платформы для сбора вакансий.
    Платформы заранее выбирает пользователь.
    """
    source = user_communication.provide_platform_choice()

    keyword = user_communication.get_keyword()

    vacancies_count = user_communication.get_vacancies_count()

    hh = HHVacancyAPI()

    sj = SJVacancyAPI()

    if source == '1':
        api_response = hh.get_response(keyword, vacancies_count)
        vacancies = Vacancy.instantiate_from_hh_data(api_response)

    elif source == '2':
        api_response = sj.get_response(keyword, vacancies_count)
        vacancies = Vacancy.instantiate_from_superjob_data(api_response)

    else:
        api_response = hh.get_response(keyword, vacancies_count)
        hh_vacancies = Vacancy.instantiate_from_hh_data(api_response)

        api_response = sj.get_response(keyword, vacancies_count)
        sj_vacancies = Vacancy.instantiate_from_superjob_data(api_response)

        vacancies = hh_vacancies + sj_vacancies

    return vacancies


def json_manipulator(vacancies):
    """
    Сохранят вакансии в формате json в файл.
    В зависимости от решения пользователя может добавлять вакансии в формате json в файл с избранными вакансиями.
    """
    user_communication.print_json_info()
    json_vacancies = JSONVacancyStorage('vacancies.json')
    json_vacancies.create_new_json_file([item.__dict__ for item in vacancies])

    favorites_vacancies = user_communication.saving_to_json()
    if favorites_vacancies:
        json_favorites_vacancies = JSONFavoritesVacancies()
        favorites_vacancies = favorites_vacancies.split(', ')

        for vid in favorites_vacancies:
            vacancy = json_vacancies.get_vacancy_by_id(int(vid))
            if vacancy is None:
                print(f'Не найдено вакансии с ID - {vid}')

            else:
                json_favorites_vacancies.add_vacancy(vacancy)

            print('Найденные вакансии добавлены в "favorites_vacancies.json"\n')


if __name__ == '__main__':
    main()
