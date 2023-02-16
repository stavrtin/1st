import os

import controller
import datetime
import time

def cls():
   os.system("cls")






def show_main_menu():
    os.system("cls")
    '''главное меню'''
    main_menu = {1: 'Открыть записную',
                 2: 'Добавить запись',
                 3: 'Удалить запись',
                 4: 'Редактировать запись',
                 5: 'Сохранить записную',
                 6: 'Найти запись',
                 7: 'Выход'
                  }
    for key, value in main_menu.items():
        print(f'{key} - {value}')
    while True:
        try:
            item_menu = int(input("Выберите пункт работы с записной >>   "))
            if item_menu not in main_menu:
                raise Exception
            return item_menu
        except Exception:
            print('Ошибка ввода. Введите правильное значение ')

    return item_menu


def input_new_record():
    imput = (input('Введите заголовок и собственно заметку, отделяя части двумя слеш: заголовок // содержание заметки >>  '))
    new_record = [imput.split('//')[0], imput.split('//')[1], time.strftime("%Y-%m-%d %H:%M")]
    return new_record


def select_del_record():
    id_del_record = (input('Введите id номера записи >>  '))

    return id_del_record



def sub_menu_save():
    '''подменю сохранения в выбранный формат'''

    main_menu = {1: 'Сохранить в .txt',
                 2: 'Сохранить в .csv',
                 3: 'Сохранить в .json',
                 4: 'Вернуться в предыдущее меню'
                  }
    for key, value in main_menu.items():
        print(f'{key} - {value}')
    while True:
        try:
            item_menu = int(input("Выберите формат сохранения записной >>   "))
            if item_menu not in main_menu:
                raise Exception
            return item_menu
        except Exception:
            print('Ошибка ввода. Введите правильное значение ')

    return item_menu

def sub_menu_open():
    '''подменю сортировка по какому полю?'''

    print('Выводим записную книгу')
    with open('notebook.csv', 'r', encoding='utf8') as f:
        text = f.read()
    print(text)
    str(input("Для возврата в главное меню - нажмите   ENTER   "))
    controller.main_process()


def message_convert_to_json():
    print('Экспортируем книгу в json формат')

def message_convert_to_csv():
    print('Экспортируем книгу в csv формат')



def input_new_record_completed():
    print('Запись добавлена')