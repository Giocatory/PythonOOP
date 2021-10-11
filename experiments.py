class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)
        self.values.sort()

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Сложение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        new_v = []
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('Умножение векторов разной длины недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя умножать с {other}')