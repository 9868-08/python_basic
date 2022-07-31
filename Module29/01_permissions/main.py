"""Напишите декоратор `check_permission`, который проверяет, есть ли у пользователя доступ к вызываемой функции, и если нет, то выдаёт исключение `PermissionError`.
"""
import functools
from functools import wraps
from collections.abc import Callable


def check_permission_with_user(input_user: str = None) -> Callable:
    def check_permission(fn: Callable) -> Callable:

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
    return check_permission


@check_permission_with_user('admin')
def delete_site(input_user=None):
    print('Удаляем сайт')
    return


@check_permission_with_user('user_1')
def add_comment(input_user=None):
    print('Добавляем комментарий')


delete_site()
try:
    add_comment()
except PermissionError:
    print("У пользователя нет прав на это действие")
