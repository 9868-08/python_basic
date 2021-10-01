# TODO: Прочитайте ещё раз внимательно алгоритм.
#  Вы сделали совершенно не то, что я вам описывал.
#  Алгоритм:
#  - запрашиваем максимальное число max_number
#  - объявляем переменную all_nums всех чисел от 1 до max_number all_nums,
#  которая равна множеству set() от range() от 1 до max_number + 1
#  - объявляем переменную возможных чисел possible_nums, равную all_nums
#  - объявляем бесконечный цикл
#  - в цикле:
#      - запрашиваем предполагаемые числа guess, которые вводятся через пробел
#      (Пример: Нужное число есть среди вот этих чисел: 1 2 3 4 5)
#      - проверяем, если guess равно 'Помогите!', то делаем break
#      - создаем множество guess, который получаем с помощью set comprehension по guess.split(),
#      переменная цикла i_num, в множество будет добавляться int(i_num)
#      - запрашиваем ответ answer, приводим его к нижнему регистру
#      - проверяем, если answer равно 'да', то берем пересечение possible_nums с guess с заменой possible_nums
#      (делается с помощью оператора &=),
#      иначе - берем разность possible_nums с guess с заменой possible_nums (делается с помощью оператора -=)
#  - печатаем числа, которые мог загадать Артем, - сортированные possible_nums
from random import randint

# max_number = int("Введите максимальное число: ")
max_number = 10
enigmatically = randint(1, max_number)
print('Загадано: ', enigmatically)
all_nums = {i for i in range(max_number + 1)}

possible_nums = all_nums
while 1 == 1:
	guess = input("Нужное число есть среди вот этих чисел: ")
	guess_list = set(guess)
	if guess == "Помогите!":
		break
	str_1 = "Hire the top 1% freelance developers"
	#	guess_list = guess.split()
	print(guess_list)
