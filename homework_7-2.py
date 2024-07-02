import io
from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='UTF-8')
    for line in strings:
        line_ = line + '\n'
        n = strings.index(line)
        file.write(line_)               # Записал(добавил) строку в файл file_name
        strings_positions ={(n, file.tell()):line}
        print(strings_positions)
    return strings_positions
    print(strings_positions)
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)


