fib1 = 1
fib2 = 1

num_pos = input("Номер элемента ряда Фибоначчи: ")
num_pos = int(num_pos)

i = 0
while i < num_pos - 2:
	fib_sum = fib1 + fib2
	fib1 = fib2
	fib2 = fib_sum
	i = i + 1

print("Значение этого элемента:", fib2)

