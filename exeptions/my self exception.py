# На примере вычисления площади треугольника по формуле герона
import math


def calc_square(ab, ac, bc):
    if type(ab) not in (int, float):
        raise ValueError("Введено не число")
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise ValueError("Одна из сторон треугольника меньше, либо равна '0.0'")

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s


square = calc_square(10, 10, 10)  # 43.30127018922193
# square1 = calc_square(-10, 10, 10)  # ValueError: Одна из сторон треугольника меньше, либо равна '0.0'!!!
# square2 = calc_square('ab', 10, 10)  # ValueError: Введено не число

print(square)
# print(square1)
# print(square2)
