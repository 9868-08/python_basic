def a_decorator_passing_arguments(function_to_decorate):
    def wrapped_func(arg1, arg2):  # аргументы прибывают отсюда
        print("Смотри, что функция {} получила: {} {}".format(wrapped_func.__name__,arg1, arg2))
        function_to_decorate(arg1, arg2)
        return "результат работы функции"

    return wrapped_func


@a_decorator_passing_arguments
def wrapped_func(first_name, last_name):
    print("тут моя функция что-то делает")


result = wrapped_func("arg1", "arg2")
print(result)
