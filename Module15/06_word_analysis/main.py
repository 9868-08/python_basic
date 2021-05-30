input_word = 'лава'
letter_count = 0
non_uniq_count = 0
count_inside = 0
count_outside = 0
for symbol_outside in input_word:
    for symbol_inside in input_word:
        if symbol_outside == symbol_inside and not count_outside == count_inside:
            non_uniq_count+=1
            print ('Повторяется буква', symbol_outside,symbol_inside,'в позиции',count_outside,count_inside)
        count_inside += 1
    count_outside += 1
    count_inside = 0
unique_symbol = int(len(str(input_word)) - non_uniq_count/2)
print('количество уникальных букв: ', unique_symbol)
