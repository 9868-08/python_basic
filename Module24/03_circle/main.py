import math


class Circle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.R = 1

    def square(self):
        print(math.pi * self.R ** 2)
        return


test_circle = Circle()
test_circle.square()
