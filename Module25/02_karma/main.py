from random import randint


# define Python user-defined exceptions
class TestFailed(Exception):
    pass

    def __init__(self):
        print('TestFailed exception')
        file = open('karma.log', 'w')
        file.write('TestFailed exception')
        file.close()
        return


class KillError(Exception):
    pass


class DrunkError:
    pass


class CarCrashError:
    pass


class GluttonyError:
    pass


class DepressionError:
    pass


class Life:

    def __init__(self):
        self.target_karma = 500
        self.karma = 0
#        self.exception_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

    def __str__(self):
        return self.karma


my_life = Life()
while my_life.karma < my_life.target_karma:
    try:
        fate = randint(0, 10)
        if fate == 0:
            raise TestFailed()
        else:
            my_life.karma += fate
    finally:
        pass
#        print(my_life.karma)
#        print("my_life.karma")
print(my_life.__str__())

