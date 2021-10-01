#  Создайте класс Zebra,
#  внутри которого есть метод which_stripe,
#  который поочередно печатает фразы
#  "Полоска белая", "Полоска черная",
#  начиная именно с фразы "Полоска белая"
class Zebra:
    def __init__(self):
        self.count = 0

    def which_stripe(self):
        if self.count % 2 == 0:
            print("Полоска белая")
            self.count += 1
        else:
            print("Полоска черная")
            self.count += 1


z1 = Zebra()
for _ in range(5):
    z1.which_stripe()
print()
z2 = Zebra()
for _ in range(4):
    z2.which_stripe()
