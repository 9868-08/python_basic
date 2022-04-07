from random import randint


class Entity:  # Entity - существо
    def __init__(self):
        self.name = "anonymous entity"
        self.satiety = 30
        self.happiness = 100

    def __str__(self):
        return "кто:", self.name, "сытость:", self.satiety

    def stroke_cat(self):  # погладить кота
        self.happiness += 5
        return self

    def action(self):
        self.satiety -= 10
        return

    def works(self, def_flat):
        def_flat.bedside_money += 150
        return def_flat


class Man(Entity):
    def __init__(self):
        super().__init__()
        super().__str__()
        self.name = "Anonymous Man"
        return

    def eat(self):
        self.satiety += 30
        return self

    def gaming(self):
        self.satiety += 20


class Woman(Entity):
    def __init__(self):
        super().__init__()
        super().__str__()
        self.name = "Anonymous Woman"
        return

    def eat(self):
        self.satiety += 30
        return

    def works(self, def_flat):
        def_flat.dust -= 100
        if def_flat.dust < 0:
            def_flat.dust = 0
        return def_flat

    def shopping(self, def_flat):
        self.satiety += 60
        def_flat.bedside_money -= 1000
        return def_flat


class Cat:
    name = "Barsik"
    satiety = 30

    def __init__(self):
        return

    def __str__(self):
        return "кто:", self.name, "сытость:", self.satiety


    def eat(self):
        self.satiety += 10
        return


    def tears_the_wallpaper(self, def_flat):  # кот дерет обои квартиры
        def_flat.dust += 5
        return

    def action(self):
        self.satiety -= 10


class Flat:
    bedside_money = 150  # деньги в тубмочке
    dust = 0  # грязь в доме

    def __init__(self):
        pass

    def __str__(self):
        print("в тумбе осталось {} денег, уровень грязи в доме: {} ".format(self.bedside_money, self.dust))


def print_all(def_man, def_woman, def_cat, def_flat):
    print("==================   вместе живут   ==================")
    def_man.__str__()
    print("======================================================")
    def_woman.__str__()
    print("======================================================")
    def_cat.__str__()
    print("======================================================")
    def_flat.__str__()
    print("======================================================")
    print("")
    print("")
    return


man = Man()
woman = Woman()
cat = Cat()
flat = Flat()

print_all(man, woman, cat, flat)
day = 0
while day <= 365:
    if man.satiety <= 0:
        print("================+   прошло {} дней   ==================".format(day))
        print("человек умер от голода!")
        break
    if woman.satiety <= 0:
        print("================+   прошло {} дней   ==================".format(day))
        print("жена умерла от голода!")
        break
    if flat.dust < 90:
        man.satiety -= 10
        woman.satiety -= 10
    rnd = randint(0, 6)
    if rnd == 0:  # мужу ласкать кота
        man.stroke_cat()
    elif rnd == 1:  # жене ласкать кота
        woman.stroke_cat()
    elif rnd == 2:
        man.works(flat)
    elif rnd == 3:
        flat = woman.works(flat)
    elif rnd == 4:
        cat.tears_the_wallpaper(flat)
    elif rnd == 5:
        man.gaming()
    elif rnd == 6 and flat.bedside_money > 0:
        woman.shopping(flat)

    #    print(rnd)
    day += 1
    flat.dust += 5
    man.action()
    woman.action()
    print("================+   прошло {} дней   ==================".format(day))
print_all(man, woman, cat, flat)
