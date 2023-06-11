class Vacancy:

    def __init__(self, vid, name, url, salary_from, salary_to, description, area):
        """
        Конструктор класса Vacancy.

        :param vid: ID вакансии
        :param name: Название вакансии.
        :param url: Ссылка на вакансию.
        :param salary_from: Минимальная зарплата.
        :param salary_to: Максимальная зарплата.
        :param description: Описание вакансии.
        :param area: Город.
        """
        self.vid = vid
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.area = area

    def __str__(self):
        return f'********************************\n'\
               f'{self.name}\n' \
               f'--------------------------------\n' \
               f'ID: {self.vid}\n' \
               f'{self.url}\n' \
               f'Зарплата от {self.salary_from}\n' \
               f'Зарплата до {self.salary_to}\n' \
               f'Описание: {self.description}\n' \
               f'Город: {self.area}\n'\
               f'********************************\n'

    def __gt__(self, other):
        """
        Метод сравнения вакансий между собой по зарплате("Зарплата от").
        """
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from

        raise TypeError

    @classmethod
    def instantiate_from_hh_data(cls, hh_data):
        """
        Создает список объектов класса Vacancy на основе данных о вакансиях из API hh.ru.

        :param hh_data: Список словарей с данными о вакансиях из API hh.ru.
        :return: Список объектов класса Vacancy.
        """
        vacancies_list = []

        for data in hh_data:
            if data['salary'] is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = data["salary"]["from"] if data["salary"]["from"] else 0
                salary_to = data["salary"]["to"] if data["salary"]["to"] else 0

            vacancy = Vacancy(int(data['id']), data['name'], data['alternate_url'], salary_from, salary_to,
                              f"\nТребования: {data['snippet']['requirement']}\n"
                              f"О работе: {data['snippet']['responsibility']}", data['area']['name'])

            vacancies_list.append(vacancy)

        return vacancies_list

    @classmethod
    def instantiate_from_superjob_data(cls, superjob_data):
        """
        Создает список объектов класса Vacancy на основе данных о вакансиях из API superjob.ru.

        :param superjob_data: Список словарей с данными о вакансиях из API superjob.ru.
        :return: Список объектов класса Vacancy.
        """
        vacancies_list = []

        for data in superjob_data:
            vacancy = Vacancy(data['id'], data['profession'], data['link'], data['payment_from'], data['payment_to'],
                              data['candidat'], data['town']['title'])

            vacancies_list.append(vacancy)

        return vacancies_list
