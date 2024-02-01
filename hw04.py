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