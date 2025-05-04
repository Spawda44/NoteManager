from ..utils import util as u
import datetime

# Получение всяких данных
# Тут заголовок
def titleInput() -> str:
    """_summary_

    Raises:
        Exception: Если заголовок будет пустой,
        сработает исключение.

    Returns:
        str: Название заголовка заметки.
    """
    title = input('Введите заголовок >> ')
    try:
        if title:
            return title
        else:
            raise Exception('Пустой заголовок.')
    except Exception:
        print('Заголовок не должен быть пустым!\n')
        return titleInput()

# Тут кантент
def contentInput() -> str:
    """_summary_

    Raises:
        Exception: Если содержание будет пустым,
        сработает исключение.

    Returns:
        str: Содержание заметки.
    """
    content = input('Введите содержание >> ')
    try:
        if content:
            return content
        else:
            raise Exception('Пустое содержание.')
    except Exception:
        print('Содержание не должно быть пустым!\n')
        return contentInput()

# Тут дату создания заметки
def dateInput() -> str:
    """_summary_

    Raises:
        Exception: Если пользователь выберет пункт, которого
        нет в списке, то вернёт ошибку.

    Returns:
        str: Дата создания заметки.
    """
    CHOICE_1 = 'Авто'
    CHOICE_2 = 'Пользовательская'
    
    choices = {
        '1' : CHOICE_1,
        '2' : CHOICE_2
    }
    u.read(choices, 'm')
    
    choice = input('Выберите пункт >> ')
    try:
        if choice in choices:
            if choice == '1' | choice == CHOICE_1:
                now = datetime.datetime.now().strftime('%d-%m-%Y')
                return now
            elif choice == '2' | choice == CHOICE_2:
                date = u.normalizeDate(input('Введите дату >> '))
                return date
        else:
            raise Exception('Некорректный выбор.')
    except Exception:
        print('Такого выбора нет!')
        return dateInput()

# Тут статус заметки
def statusInput() -> str:
    """_summary_

    Raises:
        Exception: Вернёт ошибку если выбранного статуса
        пользователем не существует.

    Returns:
        str: Выбранный статус заметки из списка.
    """
    statuses = {
        '1': 'Выполнено',
        '2': 'В процессе',
        '3': 'Отложено'
    }
    
    u.read(statuses)
    
    choice = input('\nВведите номер статуса >> ')
    try:
        if choice in statuses:
            return statuses.get(choice)
        else:
            raise Exception('Несуществующий заголовок.')
    except Exception:
        print('Такого заголовка не существует!')
        return statusInput()

def buildNote() -> dict:
    title       = titleInput()
    content     = contentInput()
    create_date = dateInput()
    status      = statusInput()
    
    note = {
        'Заголовок': title,
        'Содержание': content,
        'Дата создания': create_date,
        'Статус': status
    }
    return note