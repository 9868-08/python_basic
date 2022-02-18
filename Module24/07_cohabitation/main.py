from random import randrange


class Man:
    hungry = 50

    def __init__(self, name="Имя по-умолчанию", hungry=50):
        self.name = name
        self.hungry = hungry
        self.house = House()

    def info(self):
        print('сосед {} голодный: {} '.format(self.name, self.hungry))

    def def_eat(self, def_man):
        def_man.hungry += 10
        def_man.house.fridge -= 10
        return def_man

    def def_work(self, def_man):
        def_man.hungry -= 10
        def_man.house.nightstand_with_money += 10
        return def_man

    def def_buy(self, def_man):
        def_man.house.fridge += 10
        def_man.house.nightstand_with_money -= 10
        return def_man

    def def_game(self, def_man):
        def_man.hungry -= 10
        return def_man


class House:

    def __init__(self):
        self.fridge = 50
        self.nightstand_with_money = 0

    def info(self):
        print('в холодильнике осталось {} еды. В тумбочке осталось денег:  {}'.format(self.fridge, self.nightstand_with_money))



neighbor1 = Man("Артем")
neighbor2 = Man("Сережа")
my_house = House()
neighbor1.house = my_house
neighbor2.house = my_house


day = 0
while day < 365:
    action = (randrange(6))
    #    print("action=", action)
    if neighbor1.hungry < 20:
        print("на {} день первый сосед покушал, так как проголодался".format(day, neighbor1.name))
        neighbor1 = neighbor1.def_eat(neighbor1)
    elif neighbor2.hungry < 20:
        print("на {} день второй сосед покушал, так как проголодался".format(day, neighbor2.name))
        neighbor2 = neighbor2.def_eat(neighbor2)
    elif my_house.fridge < 10:
        print("на {} день они пошли в магазин".format(day))
        neighbor1 = neighbor1.def_buy(neighbor1)
        neighbor2 = neighbor2.def_buy(neighbor2)
    elif my_house.nightstand_with_money < 50:
        print("на {} день они пошли работать так как кончились деньги".format(day))
        neighbor1 = neighbor1.def_work(neighbor1)
        neighbor2 = neighbor2.def_work(neighbor2)
    elif action == 1:
        print("на {} день они пошли работать".format(day))
        neighbor1 = neighbor1.def_work(neighbor1)
        neighbor2 = neighbor2.def_work(neighbor2)
    elif action == 2:
        print("на {} день они поели".format(day))
        neighbor1 = neighbor1.def_eat(neighbor1)
        neighbor2 = neighbor2.def_eat(neighbor2)
    else:
        print("на {} день они играли".format(day))
        neighbor1 = neighbor1.def_game(neighbor1)
        neighbor2 = neighbor2.def_game(neighbor2)

    neighbor1.info()
    neighbor2.info()
    my_house.info()
    day += 1
print("========= на {0} программа закончила работу =========".format(day))
neighbor1.info()
neighbor2.info()
my_house.info()
