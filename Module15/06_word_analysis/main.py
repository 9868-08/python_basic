input_word = 'лава'
output = []
letter_count = 0
non_uniq_count = 0
count_inside = 0
count_outside = 0
for symbol_outside in input_word:
    if symbol_outside not in output:  # если символа нет в списке
        output.append(symbol_outside)
print('уникальных букв в слове', input_word, ' - ', len(output))
