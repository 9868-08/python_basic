"""
В проекте по 3D-моделированию используются две фигуры — куб и пирамида. Для моделирования этих фигур используются соответствующие 2D-фигуры, а именно квадрат и треугольник. Вся поверхность 3D-фигуры может храниться в виде списка. Например, для куба это будет [Square, Square, Square, Square, Square, Square].



Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой. Каждая из 2D-фигур умеет находить свои
периметр и площадь, а 3D-фигуры, в свою очередь, могут находить площадь своей поверхности.

"""

import math


class MySquare:

    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'сторона квадрата = ' + str(self.side)

    def periphery(self):                 # периметр
        result = self.sid * 4
        return result

    def square(self):                    # площадь
        result = self.side**2
        return result


class MyTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return 'сторона треугольника = ' + str(self.side) + 'высота треугольника = ' + str(self.height)

    def periphery(self):                 # периметр
        result = 2 * sqrt(self.base ** 2 - self.height ** 2)
        return result

    def square(self):                    # площадь
        result = self.side * self.height / 2
        return result

class Cube(MySquare):
    def __init__(self):
        self.side = MySquare.si



'''N_class = MyMath(1, 1)
print(N_class)
print("длина окружности = ", N_class.circumference_length())
print("площадь окружности = ", N_class.circumference_square())
print("объем куба = ", N_class.cube_volume())
print("объем сферы = ", N_class.sphere_square())
'''