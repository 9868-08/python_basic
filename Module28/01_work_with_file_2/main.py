"""Реализуйте модернизированную версию контекст-менеджера File:

- теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи;
- на выходе из менеджера подавляются все исключения, связанные с файлами.
"""


def open_file(def_filename: str) -> object:
    try:
        def_work_file = open(def_filename, 'w')

    except FileNotFoundError:
        print('Файл не найден!\tСоздается новый')
        new_file = open('test_file.txt', 'x')
        new_file.write("")
        new_file.close()
        new_file = open('test_file.txt', 'w')
        return new_file

    finally:
        print('файл {} открыт для записи'.format(def_filename))
        return def_work_file


filename = "test_file.txt"
work_file = open_file(filename)
work_file.write("01_work_with_file_2")
work_file.close()

