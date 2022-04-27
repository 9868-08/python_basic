def count(func: object):
    """
    Декоратор - счётчик
    :type func: object
    """

    counters = {}

    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)

    return wrapper


@count
def double_function(a):
    """
    Умножаем полученный параметр.
    """
    return a * 2


@count
def triple_function(a):
    """
    Утраиваем
    """
    return a * 3


if __name__ == "__main__":
    print(list(map(double_function, range(2))))
    print(list(map(triple_function, range(4))))
    print(list(map(double_function, range(10, 11))))
    print(list(map(triple_function, range(12, 13))))