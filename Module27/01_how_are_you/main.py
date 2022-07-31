from functools import wraps


def how_are_you(fn):
    def wrapped():
        input("как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return fn()

    return wrapped


@how_are_you
def test():
    return "Тут что-то происходит...>"


print(test())
