from abc import ABC, abstractmethod


class FileDataManager(ABC):
    """
    Абстрактный класс для работы с данными о вакансиях в файле.
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Абстрактный метод для добавления вакансии в файл.
        """
        pass

    @abstractmethod
    def get_vacancy_by_id(self, vid):
        """
        Абстрактный метод для получения вакансии из файла по идентификатору.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vid):
        """
        Абстрактный метод для удаления вакансии из файла по идентификатору.
        """
        pass
