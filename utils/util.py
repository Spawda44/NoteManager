def normalizeDate(date: str) -> str:
    date = date.replace('.', '-').replace('/', '-').replace('\\', '-')
    return date

def read(note: dict, type: str='n') -> None:
    """_summary_

    Args:
        note (dict): Заметка или меню в формате словаря, где key -
        это подзаголовок (или номер пункта меню),
        а value - содержание.
        
        type (str, optional): 'm' - чтение меню,
        'n' - чтение заметки.
        Defaults to 'n'.
    """
    try:
        if type == 'n':
            for key, value in note.items():
                print(f'{key}: {value}')
        elif type == 'm':
            for key, value in note.items():
                print(f'[{key}] - {value}')
        else:
            print('- Тип словаря некорректен! -')
    except AttributeError:
        print('- Заметка некорректна! -')

# Дебаг
def debug() -> None:
    from faker import Faker
    fake = Faker('ru_RU')
    
    # Нормальное состояние
    try:
        note = {
            'ФИО': fake.name(),
            'Номер телефона': fake.phone_number(),
            'Место проживания': fake.city()
        }
        read(note)
    except:
        print('Что-то не так.')
    
    # # Неправильный словарь в качестве первого аргумента mote
    # note = [fake.name(), fake.phone_number(), fake.city()]
    # read(note)
    
    # Неправильный тип в качестве второго аргумента type
    note = {
            'ФИО': fake.name(),
            'Номер телефона': fake.phone_number(),
            'Место проживания': fake.city()
        }
    read(note, 'y')

if __name__ == '__main__':
    try:
        debug()
    except KeyboardInterrupt:
        print('End program.')