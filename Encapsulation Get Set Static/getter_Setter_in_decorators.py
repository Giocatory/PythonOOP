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
    def __get__(self):
        return self.__bonus


ch = Character()
print(ch.bonus)  # 10
ch.bonus = 1000
print(ch.bonus)  # 1000
print(ch.__get__)  # 1000
