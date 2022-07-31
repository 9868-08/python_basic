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


N = 0
while N == 0:
    try:
        N = int(input("введите число N: "))
    except ValueError:
        print("нужно целое ввести число (тип int)")
# N = 10
N_class = Func(N)
print(N_class)
print("")
