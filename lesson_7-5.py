import os
import time
import termcolor
from termcolor import colored, cprint
# import colorama
# colorama.init()

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")


print('Текущая директория: ', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')                      # не позволяет создать вложенных структур. для этого makedirs
    os.chdir('second')                      # перекидывает в папку. а makedirs создает но не перекидывает
print('Текущая директория: ', os.getcwd())
# os.makedirs(r'third\fourth\fifth')
# os.chdir('fifth')
print('Текущая директория: ', os.getcwd())
print('Список папок внутри: ', os.listdir())    # показал только одну папку без вложенностей

for i in os.walk('.'):
    print(i)
print('Текущая директория: ', os.getcwd())

os.chdir(r'D:\Python_lessons\pythonProject0\Модуль 7')
print('Текущая директория: ', os.getcwd())
print('Список папок внутри: ', os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dir = [d for d in os.listdir() if os.path.isdir(d)]
print(dir)
print(file)
os.startfile(file[1])
print(os.stat(file[1]))
print(os.stat(file[1]).st_atime)
os.system('pip install random2')
os.system('pip install termcolor')

# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))