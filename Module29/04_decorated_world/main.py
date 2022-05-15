#Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая
#должна быть декоратором, и даёт возможность любому декоратору принимать произвольные
# аргументы.
# decorator_with_args_for_any_decorator это декоратор для декораторов. Это решение из
# Module29\01_permissions подходит для решения задачи

import functools
from functools import wraps
from collections.abc import Callable


def decorator_with_args_for_any_decorator(input_user: str = None) -> Callable:
    def decorated_decorator(fn: Callable) -> Callable:

        @functools.wraps(fn)
        def wrapped():
            users = ['admin', 'user']
            if input_user in users:
                print("доступ для выполнения {} разрешен".format(fn))
            else:
                print("доступ для выполнения {} запрещен".format(fn))
                raise PermissionError

            return fn()
        return wrapped
    return decorated_decorator


@decorator_with_args_for_any_decorator('admin')
def delete_site(input_user=None):
    print('Удаляем сайт')
    return


@decorator_with_args_for_any_decorator('user_1')
def add_comment(input_user=None):
    print('Добавляем комментарий')


delete_site()
try:
    add_comment()
except PermissionError:
    print("У пользователя нет прав на это действие")
