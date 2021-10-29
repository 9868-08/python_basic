def my_func(num_finish):
	num = 1
	while num != num_finish+1:
		print(num)
		num += 1


finish = int(input("Введите конечное число: "))
my_func(finish)
