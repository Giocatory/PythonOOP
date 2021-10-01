# Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты
# brand, model, price
# и также атрибут laptop_name - строковое значение, вида "<brand> <model>"
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"


laptop1 = Laptop('Asus', '18-bugfix', 37000)
print(laptop1.laptop_name)
