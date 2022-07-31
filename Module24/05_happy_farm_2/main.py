class Gardener:

    def __init__(self, name="Bob", row=1):
        self.name = name
        self.row = row

    def take_care(self, potato):  # ухаживать за грядкой
        self.potato = potato
        potato.maturity+=1
        return potato


    #        row.

    def harvest(self, row):  # собирать урожай
        self.row = row


class Potato:

    def __init__(self, raw=0, maturity=0):
        self.raw = raw  # номер грядки
        self.maturity = maturity  # maturity - стадия зрелости (всего их 4)

    def info(self, raw=1):
        print("Картофель на грядке {} созрел до стадии {}".format(raw, str(self.maturity)))


def all_potato_maturity(def_potato_list):
    for potato in def_potato_list:
        potato.info()
    return


first_raw = 1
first_gardner = Gardener()

potato_list = list()
for i in range(0, 5):       # высаживаю 5 картофеля на грядку 1
    potato_list.append(Potato())
    potato_list[0].raw = 1


while True:
    print("\n\n === настапил следующий день === ")
    all_potato_maturity(potato_list)
    for i_potato in potato_list:
        first_gardner.take_care(i_potato)
    if i_potato.maturity == 5:
        break
print("\n\n === настапил следующий день === ")
all_potato_maturity(potato_list)
