# Напишите функцию, которая находит его наименьший делитель, отличный от 1.
def smallest_diveder(num):
    div = 2
    result = num
    while div < num / 2 + 1:
        if num % div == 0:
            result = div
        div += 1
    return result


inc = 27
print(smallest_diveder(inc))
