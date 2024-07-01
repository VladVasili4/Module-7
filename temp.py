from pprint import pprint
class Product:

    def __init__(self, name, weight, category):      #weight, category
        self.name = name
        self. weight = 'weight'
        self.category = category
        # self.v = str(self.name, self. weight, self.category)

    def __str__(self):
        return f'{self.name}, {self. weight}, {self.category}'

# s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
print(p1)
print(p3)
