alphabet = 'abcdefg'

alphabet_copy=alphabet[:]
print('1. Копия строки:',alphabet_copy)
print('2. Элементы строки в обратном порядке:',alphabet[::-1])
print('3. Каждый второй элемент строки (включая самый первый):',alphabet[::2])
print('4. Каждый второй элемент строки после первого:',alphabet[1::2])
print('5. Все элементы до второго:',alphabet[:2])
print('6. Все элементы начиная с конца до предпоследнего:',alphabet[:len(alphabet)-3:-1])
print('7. Все элементы в диапазоне индексов от 3 до 4 (не включая 4):',alphabet[2:3])
print('8. Последние три элемента строки',alphabet[4:])
print('9. Все элементы в диапазоне индексов от 3 до 4 (не включая 5)',alphabet[2:4])
alphabet_small=alphabet[2:4]    # использую меременну для присвоения промежуточного результата
print('10. То же, что и в предыдущем, но выводится в обратном\n порядке.',alphabet_small[::-1],)
print('я не понял, почему alphabet[2:4:-1] не работает',alphabet[2:4:-1])