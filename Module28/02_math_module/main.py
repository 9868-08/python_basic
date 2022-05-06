"""Реализуйте класс `MyMath`, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

- вычисление длины окружности,
- вычисление площади окружности,
- вычисление объёма куба,
- вычисление площади поверхности сферы.
"""

import math


class MyMath:

    def __init__(self, radius, side):
        self.radius = radius
        self.side = side

    def __str__(self):
        return 'радиус = ' + str(self.radius) + '\tсторона = ' + str(self.side)

    def circumference_length(self):
        result = 2 * math.pi * self.radius
        return result

    def circumference_square(self):
        result = math.pi * self.radius ** 2
        return result

    def cube_volume(self):
        result = self.side ** 3
        return result

    def sphere_square(self):
        result = 4 * math.pi * self.radius ** 2
        return result


N_class = MyMath(1, 1)
print(N_class)
print("длина окружности = ", N_class.circumference_length())
print("площадь окружности = ", N_class.circumference_square())
print("объем куба = ", N_class.cube_volume())
print("объем сферы = ", N_class.sphere_square())
