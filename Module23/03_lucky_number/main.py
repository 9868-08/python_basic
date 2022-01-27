summ = 0
try:
    file_output = open('customer_input.txt', 'w')

    while True:
        customer_input = int(input('Введите число: '))
        summ += customer_input
        result = "Введено число: " + str(customer_input) + ". сумма всех введенных чисел: " +  str(summ)
        print(result)
        file_output.write(result+'\n')
        if summ >= 777 or customer_input == "exit":
            break


except ValueError:
    print('Вы ввели не число. Программа завершена')
finally:
    file_output.close()
