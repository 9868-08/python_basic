class Cards:
    card_values = {"2": 2,
                   "3": 3,
                   "4": 4,
                   "5": 5,
                   "6": 6,
                   "7": 7,
                   "8": 8,
                   "9": 9,
                   "10": 10,
                   "11": 10,  # король
                   "12": 10,  # королева
                   "13 ": 10,  # валет
                   "14": 11}  # туз

    def __init__(self):
        return

    def summ(self, cards_list):
        def_sum = 0
        for i_card in cards_list:
            if i_card % 10 == 0:
                def_sum += i_card
            elif i_card == 14 and def_sum < 21:
                def_sum += 11
            elif i_card == 14 and def_sum > 21:
                def_sum += 1
            print("текущая карта", i_card)
        return def_sum


from random import randrange

my_cards_list = []
new_card = Cards()
for i_card in range(1, 3):
    new
    my_cards_list.append(randrange(14))
#    temp = randrange(14)
#    temp = 14
#    print(i_card, temp, card_valuses.get(str(temp)))
print(my_cards_list)
my_cards_list.su
