class TestFailed(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class KillError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class KillError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


import random

errors = [KillError, DrunkError, CarCrashError, GluttonyError]
err = []
try:
    if random.randint(1, 10) == 1:
        raise (KillError, DrunkError, CarCrashError, GluttonyError)
except (KillError, DrunkError, CarCrashError, GluttonyError) as e:
    with open('karma.log', 'r') as file:
        e = file.readlines()
    err.append((random.choice([KillError, DrunkError, CarCrashError, GluttonyError]) + '\n'))
    with open('karma.log', 'w') as file:
        for i in err:
            file.write(str(i))
print(random.randint(1, 7))
