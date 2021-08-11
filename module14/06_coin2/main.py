# Даны два действительных числа x и y и радиус r.
def search_result(x, y, r, x_c, y_c):
    x=x_c-x
    y=y_c-y
    if x**2+y**2<r**2:
        return 1
    else:
        return 0

x = 1
y = 8
r = 10
x_c = -1
y_c = -1
if search_result(x, y, r, x_c, y_c) == 1:
    print('Точка лежит внутри круга')
else:
    print('Точка не лежит внутри круга')
