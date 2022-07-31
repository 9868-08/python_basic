def my_func(num_start, num_finish):
	num = num_start
	if num != num_finish+1:
		print(num)
		num += 1
		my_func(num,num_finish)


finish = int(input("Введите конечное число: "))
my_func(1,finish)
