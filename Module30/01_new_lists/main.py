from typing import List

'''Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.'''
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
print(list(map(lambda x: round(x ** 3, 3), floats)))

'''Из списка names берутся только те имена, в которых есть минимум пять букв.'''
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
print(list(filter(lambda x: len(x) > 4, names)))

'''Из списка numbers берётся произведение всех чисел.'''
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
from functools import reduce  # Функция для свёрки последовательности
print(reduce(lambda a, b: a * b, numbers))