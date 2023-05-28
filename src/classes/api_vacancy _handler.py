from abc import ABC, abstractmethod

import requests


class APIVacancyHandler(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(APIVacancyHandler):
    def get_vacancies(self):
        pass


class SuperJobAPI(APIVacancyHandler):
    def get_vacancies(self):
        pass
