import requests

from constants import SJ_VACANCY_URL, SUPERJOB_API_KEY
from src.classes.api_vacancy_handlers.api_vacancy_handler import APIVacancyHandler
from src.classes.api_vacancy_handlers.pages_count_mixin import PagesCountMixin


class SJVacancyAPI(APIVacancyHandler, PagesCountMixin):
    """
    Класс для работы с API HeadHunter для получения вакансий.
    """
    def __init__(self):
        """
        В методе инициализации создается атрибут `headers`, который содержит заголовки запроса к API SuperJob.
        """
        self.headers = {"X-Api-App-Id": SUPERJOB_API_KEY}

    def get_response(self, keyword: str = None, vacancies_count: int = 0):
        """
        Метод для получения списка вакансий из API Superjob.

        :param keyword: Ключевое слово для поиска по вакансиям.
        :param vacancies_count: Количество вакансий для вывода.
        :return: Список словарей с данными о вакансиях.
        """

        pages_count = self.get_pages_count(vacancies_count)

        params = {'keyword': keyword,
                  'page': 0,
                  'count': vacancies_count if vacancies_count <= 100 else 100,
                  'order_field': 'date',
                  'country': 'Россия'
                  }

        response = []

        for page in range(pages_count):
            params.update({'page': page})
            data = requests.get(SJ_VACANCY_URL, params=params, headers=self.headers)
            response += data.json()['objects']

        return response
