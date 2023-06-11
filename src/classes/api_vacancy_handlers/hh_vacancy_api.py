import requests

from constants import HH_VACANCY_URL
from src.classes.api_vacancy_handlers.api_vacancy_handler import APIVacancyHandler
from src.classes.api_vacancy_handlers.pages_count_mixin import PagesCountMixin


class HHVacancyAPI(APIVacancyHandler, PagesCountMixin):
    """
    Класс для работы с API HeadHunter для получения вакансий.
    """
    def get_response(self, keyword: str = None, vacancies_count: int = 0) -> list:
        """
        Метод для получения списка вакансий из API HeadHunter.

        :param keyword: Ключевое слово для поиска по вакансиям.
        :param vacancies_count: Количество вакансий для вывода.
        :return: Список словарей с данными о вакансиях.
        """

        pages_count = self.get_pages_count(vacancies_count)

        params = {'text': keyword,
                  'page': 0,
                  'per_page': vacancies_count if vacancies_count <= 100 else 100,
                  'order_by': 'publication_time',
                  'area': 113
                  }

        response = []

        for page in range(pages_count):
            params.update({'page': page})
            data = requests.get(HH_VACANCY_URL, params=params)
            response += data.json()['items']

        return response
