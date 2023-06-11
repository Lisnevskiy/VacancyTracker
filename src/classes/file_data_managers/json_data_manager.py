import json


class JSONVacancyStorage:
    def __init__(self, filename):
        self.filename = filename

    def create_new_json_file(self, vacancies: list) -> None:
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)

    def get_vacancy_by_id(self, vid: int):
        with open(self.filename, 'r', encoding='UTF-8') as f:
            vacancies = json.load(f)
            for vacancy in vacancies:
                if vacancy['vid'] == vid:
                    return vacancy
