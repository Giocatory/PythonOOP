class Character:
    def __init__(self):
        self.__bonus = 10

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    @bonus.getter
    def get_bonus(self):
        return self.__bonus


ch = Character()
print(ch.bonus)
ch.bonus = 1000
print(ch.bonus)
print(ch.get_bonus)
