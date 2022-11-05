
import interface


def add_note():
    summ_string = input(interface.input_surname) + " " + \
            input(interface.input_name) + " " + \
            input(interface.input_lastname) + " " + \
            input(interface.input_telephone_number) + " " + \
            input(interface.input_extra_data)
    with open('phone_base.csv', 'a', encoding='utf-8') as file:
        file.write(summ_string + '\n')
    print(f'\n {interface.result_to_add} \n {summ_string}')


def print_list(): 
    print(f'{interface.result_to_view} \n')
    with open('phone_base.csv', 'r', encoding='utf-8') as base:
        print(base.read())


def exit_program():
    print(interface.result_to_exit)


def import_format_1():
    name = input("Введите имя файла CSV (без расширения) ")
    with open(name + ".csv", "r", encoding='utf-8') as file1:
        data = file1.readlines()
    user_file_data = "".join(data)
    with open("phone_base.csv", "a",  encoding='utf-8') as file2:
        file2.write(user_file_data)
    print(interface.result_to_import_format1)


def export_format_1():
    name = input("Введите название для файла CSV (без расширения) ")
    with open("phone_base.csv", "r", encoding='utf-8') as file1:
        data = file1.readlines()
    user_file_data = "".join(data)
    with open(name + ".csv", "w",  encoding='utf-8') as file2:
        file2.write(user_file_data)
    print(interface.result_to_export_format1)


# def import_format_2():
#     import json
#     name = input("Введите имя файла JSON (без расширения) ")
#     with open(name + ".json", "r", encoding='utf-8') as file1:
#         data = json.loads(file1)
#     user_file_data = "".join(data)
#     with open("phone_base.csv", "a",  encoding='utf-8') as file2:
#         file2.write(user_file_data)
#     print(interface.result_to_import_format1)


# def export_format_2():
#     name = input("Введите название для файла JSON (без расширения) ")
#     with open("phone_base.csv", "r", encoding='utf-8') as file1:
#         data = file1.readlines()
#     user_file_data = "".join(data)
#     with open(name + ".json", "w",  encoding='utf-8') as file2:
#         file2.write(user_file_data)
#     print(interface.result_to_export_format1)


def search_surname():
    import io
    surname = input(interface.input_surname)
    with io.open('phone_base.csv', 'r', encoding='utf-8') as file:
        search = False
        for line in file:
            if surname in line:
                print(line, end='\n')
                search = True
        if not search:
            print(f'\n {interface.result_not_contact}')


def delete_entry():
    import re
    delete = input(interface.delete_surname)
    with open('phone_base.csv', 'r', encoding='utf-8') as file:
            search = False
            for line in file:
                if delete in line:
                    search = True
            if not search:
                print(f'\n {interface.result_not_contact}')
            else:
                print(f'\n {interface.result_to_delete}')
    with open('phone_base.csv', 'r', encoding='utf-8') as file1:
        notes = file1.readlines()
    pattern = re.compile(re.escape(delete))
    with open('phone_base.csv', 'w', encoding='utf-8') as file2:
        for line in notes:
            if pattern.search(line) is None:
                file2.write(line)
        


def goback_menu():
    input(f'\n Нажмите ввод для выхода в меню ')

