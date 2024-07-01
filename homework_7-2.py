from pprint import pprint
import io

"""Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' ."""






class Shop:
    __file_name = 'products.txt'

    def __str__(self):
        return f'{self.products}'
        pass

    def get_products(self):
        gruz = open(self.__file_name, 'r')
        print(gruz)
        for line in gruz:
            pprint(line)
            self.add()
        gruz.close()
    def add(self, *products):
        self.products = products.__str__()
        print('self.products @@@ :', self.products)
        tovar = open(self.__file_name, 'a')
        tovar.write(self.products)
        input('stop')
        # tovar.append(self.products)
        print(tovar)
        tovar.__str__()
        input('stop1')
        for line in tovar.__str__():
            print(line)
        tovar.close()
        pass


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self. weight = 'weight'
        self.category = category
        # self.v = str(self.name, self. weight, self.category)
    def __str__(self):
        return f'{self.name}, {self. weight}, {self.category}'

    # Shop.add(self.name, self. weight)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
print(p1)
input('yyy')
s1.add(p1, p2, p3)
print(s1.get_products())
