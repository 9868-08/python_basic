import random


class TestFailed(Exception):
    def __init__(self):
        self.message = "TestFailed"

    def __str__(self):
        return self.message


class KillError(Exception):
    def __init__(self):
        self.message = "KillError"

    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self):
        self.message = "DrunkError"

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self):
        self.message = "CarCrashError"

    def __str__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self):
        self.message = "GluttonyError"

    def __str__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self):
        self.message = "DepressionError"

    def __str__(self):
        return self.message


errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
err = []
try:
    if random.randint(1, 10) == 1:
        raise KillError('KillError')
except (KillError("1"), DrunkError, CarCrashError, GluttonyError) as e:
    with open('karma.log', 'r') as file:
        e = file.readlines()
    err.append((random.choice([KillError, DrunkError, CarCrashError, GluttonyError]) + '\n'))
    with open('karma.log', 'w') as file:
        for i in err:
            file.write(str(i))
#print(random.randint(1, 7))


def one_day():
    errors = [KillError, DrunkError, CarCrashError, GluttonyError]
    err = []
    try:
        if random.randint(1, 10) == 1:
            my_error = random.choice(errors)
            print(my_error.__str__)
            raise my_error

    except (KillError, DrunkError, CarCrashError, GluttonyError) as e:
        with open('karma.log', 'r') as file:
            e = file.readlines()
        err.append((str(random.choice([KillError, DrunkError, CarCrashError, GluttonyError])) + '\n'))
        with open('karma.log', 'w') as file:
            for i in err:
                file.write(str(i))
    return random.randint(1, 7)


KARMA = 500
life_karma = 0
while life_karma <= KARMA:
    life_karma += one_day()
print(life_karma)
