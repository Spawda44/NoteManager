'''================= en
Note Manager

version: v1.0.0
author: spawda44
================= ru
Менеджер заметок

версия: v1.0.0
автор: spawda44
'''

import datetime as dt

class NoteManager(object):
    '''================= en
    It is created in a single copy, stores in itself
    sheet with notes, with the help of methods can
    read all notes and add new ones.
    ================= ru
    Создаётся в единственном экземпляре, хранит в себе
    лист с заметками, с помощью методов может читать все
    заметки и добалять новые.
    '''
    notes: list = []

    def add(self, note: 'Note') -> None:
        NoteManager.notes.append(note)

    def read(self) -> None:
        NoteManager.notesOut()
    
    @staticmethod
    def notesOut(notes_list: list) -> None:
        for i, note in enumerate(notes_list, 1):
            print(f'{'='*10}\nЗаметка #{i}\n{'='*10}')
            Note.read(note)

class Note(object):
    '''================= en
    A note can be created in an infinite number time,
    it means storing them in the Manager's storage
    NoteManager notes.
    ================= ru
    Заметка, может создаваться в бесконечном количестве
    раз, подразумевается хранение их в хранилище Менеджера
    заметок NoteManager.
    '''
    def __init__(
        self,
        title: str,
        content: str,
        create_date: dt,
        status: str
    ) -> None:
        self.title = title
        self.content = content
        self.create_date = create_date
        self.status = status
    
    def read(self) -> None:
        note = {
            'Заголовок': self.title,
            'Описание': self.content,
            'Дата создания': self.create_date,
            'Статус': self.status
        }
        Note.noteOut(note, 'n')
    
    @staticmethod
    def noteOut(note: dict) -> None:
        for key, value in note.items():
            print(f'{key}: {value}')

# Вывод словарей в консоль
def menuOut(dict_: dict) -> None:
    for key, value in dict_.items():
        print(f'[{key}] - {value}')

def titleInput() -> str:
    input('Введите заголовок >> ')

def contentInput() -> str:
    input('Введите описание >> ')

def createDateInput() -> dt:
    return dt.date.today().strftime('%d-%m-%Y')

def statusInput() -> str:
    statuses = {
        '1': 'Выполнено',
        '2': 'В процессе',
        '3': 'Отложено'
    }
    
    menuOut(statuses)
    choice = input('Выберите доступный статус (1-3) >>')
    
    if choice in statuses:
        return statuses.get(choice)
    else:
        print('Выбранного статуса не существует.')
        return statusInput()

def buildNote() -> Note:
    title = titleInput()
    content = contentInput()
    create_date = createDateInput()
    status = statusInput()
    
    note = Note(
        title,
        content,
        create_date,
        status
    )
    return note
    
def main() -> None:
    nm = NoteManager()
    
    while True:
        pass
    
if __name__ == '__main__':
    main()