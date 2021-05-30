card_list = [3060, 3070, 4010, 3090, 4010, 4020]
print("Исходный список: ", card_list)
# max_card=0
card_max = 0
output_card_list = []
for card in card_list:
    if card >= card_max:
        card_max = card
for card in card_list:
    if card != card_max:
        output_card_list.append(card)
print("Итоговый список: ", output_card_list)

