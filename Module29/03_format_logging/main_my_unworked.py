import functools
from datetime import datetime
import inspect


def log_methods(str: str):
    print("str = ", str)
    def log_methods_wrapped(cls):
        print("- Запускается {}. Дата и время запуска: {} - {} ".format(cls.__name__, datetime.now().date().strftime("%Y%m%d"), datetime.now().time()))
#        print("- Запускается {}. Дата и время запуска: {} ".format(inspect. cls.__name__, datetime.utcnow()))
#        print(inspect.currentframe())

        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            if not wrapper.instance:
                wrapper.instance = cls(*args, **kwargs)
            return wrapper.instance

        wrapper.instance = None
        return wrapper

    return log_methods_wrapped


# @log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
#        print("Тут метод {}".format(self.__name__))
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
