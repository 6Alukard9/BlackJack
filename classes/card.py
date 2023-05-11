DECK = [
    "a♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "j♥", "q♥", "k♥",
    "a♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "j♦", "q♦", "k♦",
    "a♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "j♠", "q♠", "k♠",
    "a♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "j♣", "q♣", "k♣"
]


class Card:
    card_list = []

    def __init__(self, name, value):
        # Run validations to the received arguments
        assert isinstance(name, str), f'Name {name} is not a str'
        assert isinstance(value, int), f'Value {value} is not an int'

        # Assign to self object
        self.name = name
        self.value = value

        # Actions to execute
        Card.card_list.append(self)

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        return self

    def __eq__(self, other):
        if other is None or not isinstance(other, Card):
            return False
        return self.value == other.value

    @classmethod
    def set_value(cls):
        """
        It creates cards and set their value.
        Cards are added automatically to the list.
        """
        for card in DECK:
            if card[:-1] == 'a':
                Card(card, 11)
            elif card[:1] in ['k', 'q', 'j']:
                Card(card, 10)
            else:
                Card(card, int(card[:-1]))

