import re

from constants import JSON_VACANCIES, INVALID_CHOICE, YES, NO


def print_greeting():
    print('Привет!')
    print('С помощью этой программы ты сможешь получить список с информацией о вакансиях из hh.ru и superjob.ru.')
    print('Понравившиеся вакансии можно будет добавить в избранное.\n')
    input('Нажми Enter, чтобы продолжить')
    print('')


def provide_platform_choice() -> str:
    print('Введи числом из какого источника ты хочешь получить вакансии:')
    print('1 - hh.ru')
    print('2 - superjob.ru')
    print('3 - оба варианта')

    source = input()

    if source not in ('1', '2', '3'):
        print(INVALID_CHOICE)
        provide_platform_choice()
    else:
        print('Отлично!\n')
        return source


def get_keyword() -> str:
    print('Далее введи ключевое слово для фильтрации вакансий.')
    print('Если это не требуется, просто нажми Enter')

    keyword = input()

    print('Окей!\n')
    return keyword


def get_vacancies_count() -> int:
    print('Теперь введи числом какое количество вакансий ты хочешь увидеть, но не более 500.')
    print('Если было выбрано оба источника, то выбранное количество увеличивается в 2 раза.')

    while True:
        try:
            vacancies_count = int(input())
            if 0 <= vacancies_count <= 500:
                break
            else:
                print('Введенное количество отрицательное или превышает 500.')
                print('Попробуй снова:')
        except ValueError:
            print('Введено некорректное значение. Попробуй снова:')

    print('Принято!\n')
    return vacancies_count


def sort_vacancies() -> bool:
    print('Желаешь ли ты отсортировать полученные вакансии по "зарплате от":')
    print('Порядок сортировки - от большего к меньшему.\n')
    print(YES)
    print(NO)

    sorting = input()

    if sorting == '1':
        return True
    elif sorting == '0':
        return False
    else:
        print(INVALID_CHOICE)
        sort_vacancies()


def check_list_completeness(checklist: list) -> bool:
    if len(checklist) == 0:
        print('По твоему запросу не нашлось подходящих вакансий :(\n')
        return False
    else:
        return True


def print_json_info():
    print('Полученный список вакансий будет сохранен в файле формата JSON.')
    print(f'Имя файла - "{JSON_VACANCIES}"')
    print('Чтобы не потерять этот файл при новом поиске вакансий, просто переименуй его.\n')


def saving_to_json():
    print('Если тебе понравились какие-то вакансии можешь добавить их в избранное.')
    print('Чтобы это сделать введи ID вакансий разделенные запятой и пробелом.')
    print('Если это не требуется, введи цифру "0".')

    while True:
        answer = input()

        # Используется краткий синтаксис класса символов '\D', который означает "любой символ, кроме цифры".
        if re.search('\D', answer):
            print('ID должен состоять только из цифр!\n')

        elif answer == '0':
            print('Принято\n')
            return False

        elif answer is None:
            print(INVALID_CHOICE)

        else:
            return answer


def suggest_to_continue():
    print('Желаешь поискать вакансии снова?')
    print(YES)
    print(NO)

    while True:
        answer = input()

        if answer == '1':
            return True
        elif answer == '0':
            return False
        else:
            print(INVALID_CHOICE)


def print_goodbye():
    print('\nВсего хорошего!')
    print('Пусть твоя работа приносит много денежек и хорошего настроения ;)')
