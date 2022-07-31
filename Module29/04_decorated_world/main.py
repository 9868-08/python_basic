#Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая
#должна быть декоратором, и даёт возможность любому декоратору принимать произвольные
# аргументы.

from typing import Callable, Optional, Any
import functools

def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Декоратор. Даёт возможность другому декоратору принимать произвольные аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """ Декоратор. Шаблон """
    @functools.wraps(func)
    def wrapper(function_arg1: Optional[Any], function_arg2: Optional[Any]) -> Callable:
        print("Переданные арги и кварги:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """ Пример декорируемой функции """
    print("Привет", text, num)


decorated_function("Юзер", 101)
