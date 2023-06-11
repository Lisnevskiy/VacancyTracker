import math


class PagesCountMixin:
    @staticmethod
    def get_pages_count(vacancies_count: int) -> int:
        """
        Возвращает количество страниц с вакансиями на основе общего количества вакансий.

        :param vacancies_count: Общее количество вакансий.
        :return: Количество страниц с вакансиями.
        """
        return math.ceil(vacancies_count / 100)
