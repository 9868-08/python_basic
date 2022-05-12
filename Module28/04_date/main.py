class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"День: {self.day}	месяц: {self.month}	год: {self.year}	"
#        return "День: " + str(self.day) +"	Месяц: " + str(self.month) + "	Год: " + str(self.year)


    def is_date_valid(self, date: str) -> bool:
        mdy_list = date.split("-")
        day, month, year = map(int, date.split('-'))
        self.year = year
        self.month = month
        self.day = day
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year < 9999

    def from_string(self, input_date: str) -> 'Date':
        mdy_list = input_date.split("-")
        year, month, day = map(int, input_date.split('-'))
        self.year = year
        self.month = month
        self.day = day
        return

        x = input_date.split("-")
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


date = Date()
date.from_string('10-12-2077')
print(date)

print(date.is_date_valid('10-12-2077'))
print(date.is_date_valid('40-12-2077'))
