class Water:
    name = "вода"

    def info(self):
        print('класс {}'.format(self.name))

    def __add__(self, other):
        if other.name == "воздух":
            return Storm()
        if other.name == "огонь":
            return Steam()
        if other.name == "земля":
            return Dust()


class Air:
    name = "воздух"

    def info(self):
        print('класс {}'.format(self.name))

    def __add__(self, other):
        if other.name == "огонь":
            return Lightning()
        if other.name == "земля":
            return Dust()


class Fire:
    name = "огонь"

    def info(self):
        print('класс {}'.format(self.name))
    def __add__(self, other):
        if other.name == "земля":
            return Lava()


class Earth:
    name = "земля"

    def info(self):
        print('класс {}'.format(self.name))


class Storm:
    name = "шторм"

    def info(self):
        print('класс {}'.format(self.name))


class Steam:
    name = "пар"

    def info(self):
        print('класс {}'.format(self.name))


class Lightning:
    name = "молния"

    def info(self):
        print('класс {}'.format(self.name))


class Dust:
    name = "пыль"

    def info(self):
        print('класс {}'.format(self.name))


class Lava:
    name = "лава"

    def info(self):
        print('класс {}'.format(self.name))


my_water = Water()
my_air = Air()
my_fire = Fire()
my_earth = Earth()

print("=========== исходные данные ===========")
my_water.info()
my_air.info()
my_fire.info()
my_earth.info()
print("=========== после реакции между собой ===========")
print("Вода + Воздух = ", end="")
result = my_water + my_air
result.info()
print("Вода + Огонь = ", end="")
result = my_water + my_fire
result.info()
print("Вода + Земля = ", end="")
result = my_water + my_earth
result.info()
print("Воздух + Огонь  = ", end="")
result = my_air + my_fire
result.info()
print("Воздух + Земля  = ", end="")
result = my_air + my_earth
result.info()
print("Огонь  + Земля  = ", end="")
result = my_fire + my_earth
result.info()
