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