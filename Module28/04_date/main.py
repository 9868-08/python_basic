class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def __str__(self):
        return "День: " + str(self.day) +"	Месяц: " + str(self.month) + "	Год: " + str(self.year)

    def from_string(self, input):
        x = input.split("-")
        if int(x[0]) <= 31:
            self.month = int(x[0])
        else:
            print(x[0], "Ошибка - день не может быть больше 31")

        self.day = x[0]
        if int(x[1]) <= 12:
            self.month = int(x[1])
        else:
            print(x[1], "Ошибка - месяц не может быть больше 12")
        self.year = x[2]


my_date = Date()
my_date.from_string('32-12-2077')
print(my_date)

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))