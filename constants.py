import os

HH_VACANCY_URL = 'https://api.hh.ru/vacancies'
SJ_VACANCY_URL = 'https://api.superjob.ru/2.0/vacancies/'
SUPERJOB_API_KEY: str = os.getenv('SUPERJOB_API_KEY')
JSON_VACANCIES = 'vacancies.json'
JSON_FAVORITES_VACANCIES = 'favorites_vacancies.json'
INVALID_CHOICE = 'Такого значения нет в предложенных вариантах. Попробуй еще раз.\n'
YES = '1 - Да'
NO = '0 - Нет'
