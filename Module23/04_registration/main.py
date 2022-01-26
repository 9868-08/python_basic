import os


def line_check(line):
    line = line.split()
    result = ''
    #    print(line[2])
    if len(line) != 3:
        raise custom_exception_short_line
    elif not line[0].isalpha():
        raise custom_exception_isalpha
    elif line[1].find('@') == -1 or line[1].find('.') == -1:
        raise custom_exception_mail
    elif line[1].find('.') == -1 or line[1].find('.') == -1:
        raise custom_exception_mail
    elif not line[2].isdigit():
        raise custom_exception_age
    elif not 10 < int(line[2]) < 100:
        raise custom_exception_age
    return


class custom_exception(Exception):
    pass


class custom_exception_short_line(Exception):
    pass


class custom_exception_isalpha(Exception):
    pass


class custom_exception_mail(Exception):
    pass


class custom_exception_age(Exception):
    pass

try:
    file_input = open('registrations.txt', 'r')
    file_ouput_bad = open('registrations_bad.log', 'w')
    file_ouput_good = open('registrations_good.log', 'w')
except FileNotFoundError:
    print('Файл не найден!')

summ = 0

try:

    for i_line in file_input:
        print(line_check(i_line))
except custom_exception_short_line:
    result = str(line) + '   ' + str(len(line)) + ' символов'
    print (result)
except custom_exception_isalpha:
    result = str(line) + '   ' + ' содержит не только буквы'
    print (result)
except custom_exception_mail:
    result = str(line) + '   ' + ' не корректно указан e-mail'
    print (result)
except custom_exception_age:
    result = str(line) + '   ' + ' не корректно указан возраст'
    print (result)

