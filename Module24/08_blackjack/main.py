# Задаем "константы" для выявления карт.
NUM_CARDS = [str(n) for n in range(2, 11)]
PICT_CARDS = ['Валет', 'Дама', 'Король', 'Туз']
MAX_SUM = 21


# Всего там стоит сделать ряд классов: Deck, Card и Dealer


class Deck:
    def __init__(self):
        self.card_list = NUM_CARDS + PICT_CARDS
        return

    def __add__(self, right):
        # для "мёрджа" двух деков, или дека и карты.
        return

    def append(self, card):
        self.append(card)
        # добавляем карту к деку, достаточно просто, тот же аппенд к card_list

    def get_cost(self):
        return
        # сумма карт. Идём по массиву вложенному в объект и согласно константам определённым выше вычисляем всю "стоимость"

    def __len__(self):
        return len(self.card_list)

    def is_over(self):
        return self.get_cost() > MAX_SUM

    def info(self):
        for i in self.card_list:
            print(i)

my_deck = Deck()
my_deck.info()