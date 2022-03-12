from random import randint

# Задаем "константы" для выявления карт.
NUM_CARDS = [str(n) for n in range(2, 11)]
PICT_CARDS = ['Валет', 'Дама', 'Король', 'Туз']
MAX_SUM = 21


class Deck:  # вся колода карт
    def __init__(self):
        self.card_list = NUM_CARDS + PICT_CARDS
        return

    def __add__(self, right):
        # для "мёрджа" двух деков, или дека и карты.
        return

    def append(self, card):
        self.append(card)
        # добавляем карту к деку, достаточно просто, тот же аппенд к card_list


# сумма карт. Идём по массиву вложенному в объект и согласно константам определённым выше вычисляем всю "стоимость"
def get_cost(cards):
    cost = 0
    for i in cards:
        if i in NUM_CARDS:
            cost += int(i)
        elif i == 'Валет' or i == 'Дама' or i == 'Король':
            cost += 10
        elif i == 'Туз' and cost < 21:
            cost += 11
        elif i == 'Туз' and cost > 21:
            cost += 1

    return cost

    def __len__(self):
        return len(self.card_list)

    def is_over(self):
        return self.get_cost() > MAX_SUM

    def info(self):
        for i in self.card_list:
            print(i)


full_deck = Deck()  # колода одномастных карт
# карты себе
my_deck = [str(full_deck.card_list[randint(0, len(full_deck.card_list))]) for i in range(0, 2)]
print("мне выданы:   ", my_deck, "количество очков: ", get_cost(my_deck))

# карты дилеру
dealer_deck = [str(full_deck.card_list[randint(0, len(full_deck.card_list))]) for i in range(0, 2)]
print("крупье выданы:", dealer_deck, "количество очков: ", get_cost(dealer_deck))
