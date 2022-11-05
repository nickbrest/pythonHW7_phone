def show_menu():
    print('''
    Вы работаете с телефонным справочником ver. 0.0!
    ***
    Варианты действий:
    1 Добавить контакт
    2 Удалить контакт 
    3 Импортировать данные в формате CSV
    4 Импортировать данные в формате JSON
    5 Экспортировать данные в формате CSV
    6 Экспортировать данные в формате JSON
    7 Посмотреть контакты
    8 Найти контакт по фамилии
    0 Выход из справочника
      ''')


def control_menu():
    while True:
        number = input('Выберите нужное действие (введите цифру): ')
        if number.isdigit():
            number = int(number)
            if 0 <= number <= 8:
                return number
            else:
                print('Введите цифру соответствующую пункту в меню')
                continue
        print('Вы ввели не цифру! Ведите номер требуемого действия!')
        continue
