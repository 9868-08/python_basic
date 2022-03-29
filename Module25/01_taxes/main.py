class Property:
    def __init__(self, worth=100):    # worth - стоимость
        self.worth = worth


class Appartment(Property):         # квартира

    def tax(self):
        return self.worth / 1000


class Car(Property):                # машина

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):       # дача

    def tax(self):
        return worth / 500

debit = 0
while debit == 0:
    try:
        debit = int(input("Сколько денег у вас есть?   "))
    except ValueError:
        print("нужно ввести число")

property_value = 0
#debit = 15  # денег в наличии

my_appartment = Appartment()
my_appartment.worth = 0
while my_appartment.worth == 0:
    try:
        my_appartment.worth = int(input("введите стоимость квартиры   "))
    except ValueError:
        print("нужно ввести число")
#my_appartment.worth = 10000  # стоимость моего жилья

my_car = Car()
my_car.worth = 0
while my_car.worth == 0:
    try:
        my_car.worth = int(input("введите стоимость машины   "))
    except ValueError:
        print("нужно ввести число")
#car_cost = 100           # стоимость моей машины

my_CountryHouse = Appartment()
my_CountryHouse.worth = 0
while my_CountryHouse.worth == 0:
    try:
        my_CountryHouse.worth = int(input("введите стоимость дачи   "))
    except ValueError:
        print("нужно ввести число")
#countryhouse_cost = 500  # стоимость моей дачи

#print(my_appartment.tax(), my_car.tax(), my_CountryHouse.tax())
my_tax = my_appartment.tax() + my_car.tax() + my_CountryHouse.tax()
#print(my_tax)
if debit < my_tax:
    print("Для оплаты налога не зватает", my_tax - debit)
else:
    print('Сумма налога {} меньше количества денег {}'.format(my_tax, debit))
