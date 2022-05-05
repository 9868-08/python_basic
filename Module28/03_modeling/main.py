"""
В проекте по 3D-моделированию используются две фигуры — куб и пирамида. Для моделирования этих фигур используются соответствующие 2D-фигуры, а именно квадрат и треугольник. Вся поверхность 3D-фигуры может храниться в виде списка. Например, для куба это будет [Square, Square, Square, Square, Square, Square].



Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой. Каждая из 2D-фигур умеет находить свои
периметр и площадь, а 3D-фигуры, в свою очередь, могут находить площадь своей поверхности.

"""


class Square:
    """ 2D-фигуры, а именно квадрат"""
    def __init__(self, length):
        self.length = length

    def __str__(self) -> float:  # площадь квадрата
        def_surface_area = self.length ** 2
        return def_surface_area


class SurfaceAreaMixin:

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
        self.surfaces: list[Square] = [Square, Square, Square, Square, Square, Square]
        print(self.surfaces)

    def surface_area(self) -> float:
        super(Cube, self).surface_area(Square.surface_area(Square))


my_cube = Cube(2)
print("площадь  куба = ", my_cube.surface_area())

