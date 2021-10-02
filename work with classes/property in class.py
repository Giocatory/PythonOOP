class Name:
    def __init__(self, name, surname):
        self.__name: str = name
        self.__surname: str = surname

    def first_name(self):
        return self.__name.capitalize()

    def last_name(self):
        return self.__surname.capitalize()

    def full_name(self):
        return f"{self.__name.capitalize()} {self.__surname.capitalize()}"

    def initials(self):
        return f"{self.__name[0].upper()}.{self.__surname[0].upper()}"

    first_name = property(fget=first_name)
    last_name = property(fget=last_name)
    full_name = property(fget=full_name)
    initials = property(fget=initials)


a1 = Name('john', 'SMITH')
print(a1.first_name)
print(a1.last_name)
print(a1.full_name)
print(a1.initials)
