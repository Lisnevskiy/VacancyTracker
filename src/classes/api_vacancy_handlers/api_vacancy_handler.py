from abc import ABC, abstractmethod


class APIVacancyHandler(ABC):
    """
    Абстрактный базовый класс, который определяет общий интерфейс для обработчиков запросов вакансий из API.
    """
    @abstractmethod
    def get_response(self):
        """
        Абстрактный метод для получения ответа от API.

        :return: Словарь или список словарей с данными о вакансиях.
        """
        pass
