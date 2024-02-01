"""
    Модуль № 4. Завдання № 1.
    У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
 
    Наприклад:

    Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000

    Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
"""

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            salaries = [int(num) for line in f for num in line.split(',')[1:] if num.strip().isdigit()]

            total = sum(salaries)
            avg = total // len(salaries)

            return (total, avg)
           
    except FileNotFoundError:
        return 'File not found.'
    except IndexError:
        return 'Invalid format in file.'
    except Exception as e:
        return f'An arror occured: {e}'

# # Test
# total, average = total_salary("C:\\Users\\stukachov\\Documents\\salary.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

###########################################################################################################
###########################################################################################################
###########################################################################################################

'''
    Модуль № 4. Завдання № 2.
    У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, 
    його ім'я та вік, розділені комою.

    Наприклад:

    60b90c1c13067a15887e1ae1,Tayson,3
    60b90c2413067a15887e1ae2,Vika,1
    60b90c2e13067a15887e1ae3,Barsik,2
    60b90c3b13067a15887e1ae4,Simon,12
    60b90c4613067a15887e1ae5,Tessi,5

    Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників 
    з інформацією про кожного кота.
'''


def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_info = line.strip().split(',')
                cat = {'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2]}
                cats.append(cat)
            
    except FileNotFoundError:
        return 'File not found.'
    except IndexError:
        return 'Invalid format in file.'
    except Exception as e:
        return f'An arror occured: {e}'

    return cats

# Test
# cats_info = get_cats_info("C:\\Users\\stukachov\\Documents\\cats.txt")
# print(cats_info)

###########################################################################################################
###########################################################################################################
###########################################################################################################

'''
    Модуль № 4. Завдання № 4.
    Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та 
    буде відповідати відповідно до введеної команди.

    У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на 
    початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). 
    CLI достатньо просто реалізувати. Будь-який CLI складається з трьох основних елементів:


    *   Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з 
        рядка ключових слів та модифікаторів команд.
    *   Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за 
        безпосереднє виконання команд.
    *   Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та 
        повернення користувачеві відповіді від функції - handler-а.

    На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити 
    номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, 
    які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо 
    зберігати ім'я користувача, як ключ, і номер телефону як значення.
'''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "The name wasn`t found.")
    
def show_all(contacts):
    return contacts   

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            print("Good Bye!")
            break    
        elif command == 'hello':
            print("How can i help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()