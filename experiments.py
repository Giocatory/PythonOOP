class experiment:
    def __init__(self, name):
        self.__name = name

    def __set_name__(self, name):
        self.__name = name

    def __get_name__(self):
        return self.__name

    Name = property(fset=__set_name__, fget=__get_name__)


who_are_you = experiment('Mike')
print(who_are_you.Name)
who_are_you.Name = 'Mikhail'
print(who_are_you.Name)
who_are_you.__set_name__('Margo')
print(who_are_you.Name)
