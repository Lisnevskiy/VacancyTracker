import json


class JSONVacancyStorage:
    """
    Класс для работы с хранилищем вакансий в формате JSON.
    """
    def __init__(self, filename):
        """
        Инициализирует объект класса.

        :param filename: имя файла для хранения вакансий.
        """
        self.filename = filename

    def create_new_json_file(self, vacancies: list) -> None:
        """
        Создает новый файл для хранения вакансий в формате JSON.

        :param vacancies: список вакансий.
        """
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)

    def get_vacancy_by_id(self, vid: int):
        """
        Возвращает вакансию по ее идентификатору.

        :param vid: идентификатор вакансии.
        :return: вакансия с указанным идентификатором.
        """
        with open(self.filename, 'r', encoding='UTF-8') as f:
            vacancies = json.load(f)
            for vacancy in vacancies:
                if vacancy['vid'] == vid:
                    return vacancy
