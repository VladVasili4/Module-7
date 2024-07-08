import os
import time

print(os.getcwd())
os.chdir(r'F:\Python-Urban\Homeworks\Модуль 7')

for root, dirs, files in os.walk('.'):
  for file in files:
    filepath = os.getcwd() + file
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(file)


    print(parent_dir)                             #  шляпа !!!!!!!!!!!


    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

