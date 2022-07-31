from functools import wraps
import time


def how_are_you(fn):
    def wrapped():
        print("ожидание 3 секунды")
        time.sleep(3)  # Сон в 3 секунды
        return fn()

    return wrapped


@how_are_you
def test():
    return "Тут что-то происходит...>"


print(test())
