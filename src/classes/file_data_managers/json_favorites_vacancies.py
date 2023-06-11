import json

from constants import JSON_FAVORITES_VACANCIES
from src.classes.file_data_managers.abstract_file_data_manager import FileDataManager


class JSONFavoritesVacancies(FileDataManager):
    """
    Класс для работы с избранными вакансиями в JSON файле.
    """
    def __init__(self):
        self.filename = JSON_FAVORITES_VACANCIES

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в список избранных вакансий.
        """
        with open(self.filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        data.append(vacancy)
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancy_by_id(self, vid: int):
        """
        Возвращает вакансию по ее идентификатору.
        """
        with open(self.filename, 'r', encoding='UTF-8') as f:
            vacancies = json.load(f)
            for vacancy in vacancies:
                if vacancy['vid'] == vid:
                    return vacancy

    def delete_vacancy(self, vid):
        """
         Удаляет вакансию из списка избранных вакансий.
        """
        with open(self.filename, 'r', encoding='UTF-8') as f:
            vacancies = json.load(f)
            for vacancy in vacancies:
                if vacancy['vid'] == vid:
                    del vacancy
