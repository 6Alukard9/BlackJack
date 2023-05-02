# from .person_class import *
# from .table_class import *

DECK = ["5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥",
        "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥",
        "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥",
        "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥", "5♥"]

# DECK = [
#     "a♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "j♥", "q♥", "k♥",
#     "a♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "j♦", "q♦", "k♦",
#     "a♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "j♠", "q♠", "k♠",
#     "a♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "j♣", "q♣", "k♣"
# ]


class Card:
    card_list = []

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        return self

    def __eq__(self, other):
        if other is None or not isinstance(other, Card):
            return False
        return self.value == other.value

    @staticmethod
    def set_value():
        """
        It creates cards and set their value
        """
        for card in DECK:
            if card[:-1] == 'a':
                name = f'{card}'
                Card.card_list.append(Card(name, 11))
            elif card[:1] in ['k', 'q', 'j']:
                name = card
                Card.card_list.append(Card(name, 10))
            else:
                name = card
                Card.card_list.append(Card(name, int(card[:-1])))

