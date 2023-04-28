# import random
from .casino import *
from .card import *


class SharedAttr:
    def __init__(self, name):
        self.name = name
        self.hand_list = [[], [], [], []]
        self.total_list = [[], [], [], []]
        self.credit_card = 3000
        self.cash = 1000
        self.bet_list = [[], [], [], []]
        self.ace_split = 1
        self.card_split = 3
        self.dealer = False
        self.playing = False
        self.working = False

    def __str__(self):
        return self.name

    def bet(self):
        return self.bet_list[0].append(random.randint(2, 100))

    def __len__(self):
        return len(self.hand_list)

    @staticmethod
    def to_quit():
        return quit()


class Player(SharedAttr):
    PLAYERS = 1
    player_list = []
    player_counter = 0

    def __getitem__(self, item):
        if item < 0 or item > 4:
            return IndexError
        return self.hand_list[item]

    @staticmethod
    def gen_person():
        for i in range(Player.PLAYERS):
            Player.player_counter += 1
            name = f'Player {Player.player_counter}'
            Player.player_list.append(Player(name))
        return


class Dealer(SharedAttr):
    DEALERS = 5
    dealer_list = []
    dealer_counter = 0

    @staticmethod
    def gen_person():
        for i in range(Dealer.DEALERS):
            Dealer.dealer_counter += 1
            name = f'Dealer {Dealer.dealer_counter}'
            Dealer.dealer_list.append(Dealer(name))
        return

    @staticmethod
    def imitate_shift():
        for i, dealer in enumerate(Dealer.dealer_list):
            dealer.working = True
            Casino.shift.append(dealer)




