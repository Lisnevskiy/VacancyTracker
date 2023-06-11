from abc import ABC, abstractmethod


class FileDataManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_id(self, vid):
        pass

    @abstractmethod
    def delete_vacancy(self, vid):
        pass
