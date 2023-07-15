def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента в справочнике\n"
          "6. Изменить данные абонента\n"
          "7. Закончить работу")
    choice = int(input('\nВведите номер команды: '))
    print()
    return choice

def print_top(phone_book):
    flag = True    
    for i in phone_book:
        while(flag):
            for key in i.keys():
                print(f'{key.ljust(20)}', end='')   
            print(f'\n{"-" * 80}')
            flag = False


def print_result(phone_book):
    print_top(phone_book)
    for i in phone_book:
        for value in i.values():
            print(f'{value.ljust(20)}', end='')
        print()

def get_search_name():
    return input("Введите фамилию: ")

def find_by_name(phone_book, name):
    print_top(phone_book)
    for i in phone_book:
        for key, value in i.items():
            if key == 'Фамилия':
                if value.lower() == name.lower():
                    for value in i.values():
                        print(f'{value.ljust(20)}', end='')
                    print()
                break 

def get_search_number():
    number = input("Введите номер: ")
    print()
    if number.isdigit():
        return int(number)
    else:
        print("Вы ввели некорректный номер, попробуйте еще раз")
        return get_search_number() 

def find_by_number(phone_book, number):
    print_top(phone_book)
    for i in phone_book:
        for key, value in i.items():
            if key == 'Телефон':
                if int(value) == number:
                    for value in i.values():
                        print(f'{value.ljust(20)}', end='')
                    print()
            
def get_new_user():
    new_user  = input("Введите фамилию: ") + ","
    new_user += input("Введите имя: ") + ","
    new_user += input("Введите номер телефона: ") + ","
    new_user += input("Введите примечание: ") + "\n"
    
    return new_user

def add_user(filename ,user_data):
    with open(filename, 'a+', encoding='utf-8') as fout:
        fout.write(user_data)

def delete_by_name(phone_book, name):
     for i in phone_book:
        for key, value in i.items():
            if key == 'Фамилия':
                if value.lower() == name.lower():
                    phone_book.remove(i)
                    write_csv('base_ex38.txt', phone_book)
                break 

def edit_by_name(phone_book, name):
    for i in phone_book:
        for key, value in i.items():
            if key == 'Фамилия':
                if value.lower() == name.lower():
                    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
                    edited_dict = get_new_user()
                    record = dict(zip(fields, edited_dict.strip().split(',')))
                    index = phone_book.index(i)
                    phone_book.pop(index)
                    phone_book.insert(index, record)
                    write_csv('base_ex38.txt', phone_book)
                    print()
                break 
        
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('base_ex38.txt')

    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            find_by_name(phone_book, name)
        elif choice == 3:
            number = get_search_number()
            find_by_number(phone_book, number)
        elif choice == 4:
            user_data = get_new_user()
            add_user('base_ex38.txt',user_data)
            phone_book = read_csv('base_ex38.txt')
        elif choice == 5:
            name = get_search_name()
            delete_by_name(phone_book, name)
            phone_book = read_csv('base_ex38.txt')
        elif choice == 6:
            name = get_search_name()
            edit_by_name(phone_book, name)
        elif choice > 7:
            print("Вы ввели слишком большое значение, попробуйте еще раз ")
            print()
        choice = show_menu()

def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data   

def write_csv(filename: str, data: list):                              
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')     

work_with_phonebook()    

