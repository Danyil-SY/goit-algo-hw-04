'''
    Модуль № 4. Завдання № 3.
    Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка 
    і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
    Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
'''

import sys
from pathlib import Path
from colorama import Fore, Style, init

init()

def display_structure(dir_path, indent=' '):
    directory = Path(dir_path)
    for item in directory.iterdir():
        if item.is_dir():
            print(f'{indent}{Fore.CYAN}{item.name}{Style.RESET_ALL}')
            display_structure(item, indent + ' | ')
        else:
            print(f'{indent}{Fore.YELLOW}{item.name}{Style.RESET_ALL}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python hw03.py <directory_path>')
        sys.exit(1)

    dir_path = sys.argv[1]
    try:
        display_structure(dir_path)
    except Exception as e:
        print(f'An error occured: {e}')

if __name__ == '__main__':
    main()