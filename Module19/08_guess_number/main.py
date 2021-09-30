from random import randrange

N = int(input("Введите максимальное число: "))
#N = 10
print("Введите максимальное число: ", N)
x = randrange(N)
print('загадано число',x)
answer = 0
while answer == 0:
	input_string = input("Нужное число есть среди этих чисел: ")
	if input_string == 'Помогите!':
		print("Артем загадал число: ", N)
		break
	input_list = input_string.split(' ')
	for i in input_list:
		print(i)
		if int(i) == x:
			print("Ответ Артёма: Да")
			answer = 1
			break
		else:
			print("Ответ Артёма: Нет")
