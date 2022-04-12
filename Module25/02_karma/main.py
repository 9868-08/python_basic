from random import randint


# define Python user-defined exceptions
class KillError(Exception):
    pass

    def __init__(self):
        #        print('KillError exception')
        file = open('karma.log', 'a')
        file.write('KillError exception\n')
        file.close()
        return


class DrunkError(Exception):
    pass

    def __init__(self):
        #        print('DrunkError exception')
        file = open('karma.log', 'a')
        file.write('DrunkError exception\n')
        file.close()
        return


class CarCrashError(Exception):
    pass

    def __init__(self):
        #        print('CarCrashError exception')
        file = open('karma.log', 'a')
        file.write('CarCrashError exception\n')
        file.close()
        return


class GluttonyError(Exception):
    pass

    def __init__(self):
        #        print('GluttonyError exception')
        file = open('karma.log', 'a')
        file.write('GluttonyError exception\n')
        file.close()
        return


class DepressionError(Exception):
    pass

    def __init__(self):
        #        print('DepressionError exception')
        file = open('karma.log', 'a')
        file.write('DepressionError exception\n')
        file.close()
        return


class Life:

    def __init__(self):
        self.target_karma = 500
        self.karma = 0

    def __str__(self):
        return self.karma


import os.path

log_file = "karma.log"
if os.path.exists(log_file):
    os.remove(log_file)

# Проверяем если папка существует.
os.path.exists('storage')  # True
my_life = Life()
while my_life.karma < my_life.target_karma:
    try:
        fate = randint(0, 10)
        if fate == 0:
            raise KillError
        elif fate == 1:
            raise DrunkError
        elif fate == 2:
            raise CarCrashError
        elif fate == 3:
            raise GluttonyError
        elif fate == 4:
            raise DepressionError
        else:
            my_life.karma += fate

    except KillError:
        pass
    except DrunkError:
        pass
    except CarCrashError:
        pass
    except GluttonyError:
        pass
    except DepressionError:
        pass



    finally:
        pass

print("достигнута карма: ", my_life.__str__())
