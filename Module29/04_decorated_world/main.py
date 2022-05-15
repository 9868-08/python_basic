#Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая
#должна быть декоратором, и даёт возможность любому декоратору принимать произвольные
# аргументы.

import functools
from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorator_to_enchance: Callable) -> Callable:
    """ Декоратор дает возможность другому декоратору принимать произвольные аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enchance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """" Декоратор шаблон """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print("Переданные арги в кварги в декоратор: ", dec_args, dec_kwrgs)
        return func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)