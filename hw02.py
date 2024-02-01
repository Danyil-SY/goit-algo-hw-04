'''
    Модуль № 4. Завдання № 2.
    У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний 
    ідентифікатор кота, його ім'я та вік, розділені комою.

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