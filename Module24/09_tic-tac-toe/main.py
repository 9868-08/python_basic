class Field():
    def __init__(self, x_max, y_max):
        result = list[0][0]
        for i in range(1, x_max):
            for j in range(1, y_max):
                result.append[[i], [j]] = 0
        return result

x_max = 3
y_max = 3
my_game = Field(x_max, y_max)
print(my_game)