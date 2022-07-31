class Square:
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght**2


class SurfaceAreaMixin:
    """ Класс-миксин для нахождения площади поверхности фигуры """
    def surface_area(self) -> float:
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area


class Cube(Square, SurfaceAreaMixin):
    """
    Класс Куб. Дочерний класс от Квадрата + миксин SurfaceAreaMixin

    Args:
        length (float): длина стороны

    Attributes:
        length (float): длина стороны
        surfaces (List[Square]): список из поверхностей куба (6 квадратов)
    """
    def __init__(self, length: float) -> None:
        super().__init__(length)
        self.surfaces: List[Square] = [Square, Square, Square, Square, Square, Square]


my_cube = Cube(2)
my_cube_square = Cube.surface_area(self=my_cube)
print(my_cube_square)

