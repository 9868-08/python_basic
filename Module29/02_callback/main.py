from typing import Callable

app = {}  # роутинг


def callback(url: str) -> Callable:
    def deco(response_func: Callable) -> Callable:
        if url not in app:
            app[url] = response_func

        def wrapped(*args, **kwargs):
            result = response_func(*args, **kwargs)
            return result

        return wrapped
    return deco


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


@callback('https://some_website.py')
def response():
    def func():
        def func_1():
            def func_2():
                def func_3():
                    return "Hello World"
                return func_3
            return func_2
        return func_1
    return func


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response, end='\n'*2)
else:
    print('Такого пути нет')


response = app.get("https://some_website.py")()()()()()
print(response)
