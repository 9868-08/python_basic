"""
У частных легковых автомобилей номера — это
буква, три цифры, две буквы,  две или три цифры
У такси —
две буквы, три цифры, затем две или три цифры с кодом региона.'
"""

import re

input_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_pattern = r'[А-Я]\d{3}[А-Я]{2}\d{2,3}\w'
taxi_pattern = r'[А-Я]{2}\d{3}\d{2}'

print("Список номеров частных автомобилей: ",
      re.findall(private_pattern, input_numbers))
print("Список номеров такси:: ",
      re.findall(taxi_pattern, input_numbers))