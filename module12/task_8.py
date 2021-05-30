print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
def gcd(num1, num2):       #(от англ. greatest common divisor)
    if num2 == 0:
        return num1,num2
    else:
        return gcd(num2, num1%num2)

def smolest_num(num1,num2):
        biggest=  (num1+num2+abs(num1-num2))/2
        smallest= (num1+num2-abs(num1-num2))/2
        print('минимальное число: ', (num1+num2-abs(num1-num2))/2)
        return smallest, biggest



while True:
    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    num1_num2_gcd,null = gcd (num1,num2)
    print('наибольший общий делитель двух чисел', num1, num2, 'равен: ', num1_num2_gcd)