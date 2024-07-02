import io
from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='UTF-8')
    print(file.writable())
    # Как вывести или получить номер строки 'n' для формирования словаря strings_positions
    for i in strings:
        print(i)
        n = len(strings)    #  ??????????
        file.write(i)
        print(file.tell())
        strings_positions = {(n, file.tell()): i}
    return strings_positions
    file.close()

result = custom_write('test.txt', info)
# for elem in result.items():
#     print(elem)