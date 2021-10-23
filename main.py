import random
import datetime
import os

# Набор доступных символов.
ARRAY_SYMBOLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '!', '@', '#', '$', '&', '?', '-', '+', '=', '~',
                 '_', '^', '*', '.']

# Получаем количество символов в пароле.
COUNT_SYMBOLS = 4
input_count = input("Введите количество символов в пароле: ")
if input_count.isdigit():
    count_symbols = int(input_count)
else:
    count_symbols = COUNT_SYMBOLS

# Узнаем количество всех возможных комбинаций.
count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Получить случайный символ.
def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]


print(f'Версия программы: V0.0.1')
print(f'Количество доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Доступные символы: {ARRAY_SYMBOLS}')
print(f'Количество возможных комбинаций: {count_variant}')

# Генерируем уникальный пароль.
password = ''
for i in range(0, count_symbols):
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

text_datetime = f'{datetime.datetime.now()}'
symbols_replace = ['-', ' ', ':', '.']
file_name = ''
for s in text_datetime:
    is_write = True
    for sr in symbols_replace:
        if s == sr:
            file_name += '_'
            is_write = False
    if is_write:
        file_name += s

if not os.path.exists('passwords'):
    os.mkdir('passwords')


# Запись пароля в файл.
with open(f'passwords/{file_name}_password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))

input()
