from .casino import *
# from .card import *
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

    def bet(self):
        """
        Returns random bet in the range of 2-100
        """
        return self.bet_list[0].append(random.randint(2, 100))

    def __len__(self):
        return len(self.hand_list)

    def split(self, table_name):
        """
        After getting 2 cards as initial hand, each player and NPC can separate their cards if cards are equal
        """
        if self.hand_list[0][0] == self.hand_list[0][1]:
            while True:
                if self.ace_split != 0 and self.card_split != 0:
                    self.hand_list[3 - (self.card_split - 1)].append(self.hand_list[3 - self.card_split][1])
                    self.hand_list[3 - self.card_split].pop(1)
                    bet = list(self.bet_list[0])
                    self.bet_list[3 - (self.card_split - 1)] = bet
                    table_name = Table.table_list.index(table_name)
                    if 'card' not in (Table.table_list[table_name].shoe[0], Table.table_list[table_name].shoe[1]):
                        self.hand_list[3 - self.card_split].append(table_name[0])
                        self.hand_list[3 - (self.card_split - 1)].append(table_name[1])
                        Table.table_list[table_name].shoe.pop(0)
                        Table.table_list[table_name].shoe.pop(1)
                        if self.hand_list[3 - self.card_split][0][:-1] != 'a':
                            self.card_split -= 1
                            continue
                        else:
                            self.ace_split -= 1
                            break
                    else:
                        temp_value = Table.table_list[table_name].shoe.index('card')
                        Table.table_list[table_name].shoe.pop(temp_value)
                        continue
                break

    def double_down(self):
        """
        Each player and NPC can double their bet if the total of their cards is in the range of 9-11
        """
        i = 0
        for hand in self.hand_list:
            if hand:
                if sum(e.value for e in hand) in (9, 10, 11):
                    self.bet_list[i][0] *= 2
                    if i < 3:
                        i += 1
                    else:
                        break


class NPC(SharedAttr):
    NPC = 1
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
        for i in range(NPC.NPC):
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




