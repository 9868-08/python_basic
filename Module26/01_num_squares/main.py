N = 0
while N == 0:
    try:
        N = int(input("введите число N: "))
    except ValueError:
        print("нужно целое ввести число (тип int)")
# N = 10


print("класс-итератор")


class Func:

    def __init__(self, N):
        self.__N_list = list()
        for i_counter in range(1, N + 1):
            self.__N_list.append(i_counter ** 2)

    def __str__(self):
        count = 1
        for i_item in self.__N_list:
            print(count, '\t: ', i_item)
            count += 1
        return ""


N_class = Func(N)
print(N_class, end="")

print("функция-генератор")


def func(def_N):
    for i_counter in range(1, N + 1):
        print(i_counter, "\t: ", i_counter ** 2)


func(N)

print("генераторное выражение")
my_generator = (i for i in range(1, N+1))
count = 1
for i_counter in my_generator:
    print(count, "\t: ", i_counter ** 2)
