""" N = 0
while N == 0:
    try:
        N = int(input("введите число N: "))
    except ValueError:
        print("нужно целое ввести число (тип int)")
"""

N = 10
for i_counter in range(1, N+1):
    print(i_counter, "\t: ", i_counter **2 )
