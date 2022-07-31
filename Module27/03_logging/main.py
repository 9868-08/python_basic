from functools import wraps


def logging(fn):
    def wrapped():
        try:
            return fn()
        except Exception as e:
            print("Error:", e)
            log = open('function_errors.log', 'w')
            log.write("Error: " + str(e))
            log.close()
            return "программа завершилась с ошибкой. Лог ошибки в файле function_errors.log"
    return wrapped


@logging
def my_func():
    5/0
    return "Тут что-то происходит...>"


print(my_func())