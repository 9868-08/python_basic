import math


class Circle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.R = 1

    def square(self):  # площадь круга S = π × r2
        print(math.pi * self.R ** 2)
        return

    def perimentr(self):  # периметр круга L = d*π = 2*r*π.
        print(2 * self.R * math.pi)
        return

    def intersecrion(self, x1, y1, r1):  # пересечение с окружностью x1, y1, r1
        d = math.sqrt((x1-self.x)**2+(y1-self.y)**2)
        if d < self.R+r1:
            print("окружности пересекаются")
        else:
            print("окружности не пересекаются")
        return

test_circle = Circle()
print("площадь круга = ", end="")
test_circle.square()
print("периметр круга = ", end="")
test_circle.perimentr()
#print("Во сколько раз увеличим круг?: ", end="")
#test_circle.R = int(input(""))
test_circle.R = 3
print("площадь получившегося круга = ", end="")
test_circle.square()
print("периметр получившегося круга = ", end="")
test_circle.perimentr()
x1 = 1
y1 = 1
r1 = 1
test_circle.intersecrion(x1, y1, r1)