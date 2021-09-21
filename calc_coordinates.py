# Создайте класс Point. У этого класса должны быть
# метод set_coordinates,
# который принимает координаты по x и по y, и сохраняет их в экземпляр класса
# соответственно в атрибуты x и y
# метод get_distance,
# который обязательно принимает экземпляр класса Point
# и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point
# необходимо вывести сообщение "Передана не точка"
class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, p):
        if type(p) == type(self):
            return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5
        else:
            print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
print(d)
p1.get_distance(10)
