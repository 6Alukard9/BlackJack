import random
from .casino import *
from .table_class import *


class SharedAttr:
    def __init__(self, name):
        self.name = name
        self.hand_list = [[], [], [], []]
        self.total_list = [[], [], [], []]
        self.cash = 1_000_000
        self.bet_list = [[], [], [], []]
        self.ace_split = 1
        self.card_split = 3
        self.dealer = False
        self.playing = False
        self.working = False
        self.t_name = ''

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.hand_list)


class NPC(SharedAttr):
    NPC_amount = 5
    NPC_list = []
    NPC_counter = 0

    def __getitem__(self, item):
        if item < 0 or item > 4:
            return IndexError
        return self.hand_list[item]

    @staticmethod
    def gen_npc():
        """
        Returns the required number of NPCs
        """
        for i in range(NPC.NPC_amount):
            NPC.NPC_counter += 1
            name = f'NPC {NPC.NPC_counter}'
            NPC.NPC_list.append(NPC(name))
        return


class Dealer(SharedAttr):
    DEALERS = 5
    dealer_list = []
    dealer_counter = 0

    @staticmethod
    def gen_dealer():
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




