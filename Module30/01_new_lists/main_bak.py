"""Каждое число из списка floats возводится в третью степень и округляется до"""
'''трёх знаков после запятой.'''


from typing import List

floats: List[int] = [1, 2, 3]
res: List[int] = []
print("значения массива {} в третьей степени: ".format(floats), end="")
for i_num in floats:
    res.append(i_num ** 3)
print(res
      # list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
      )
print("с использование lambda:", end=" ")
res = list(map(lambda floats: floats ** 3, floats))
print(res)
