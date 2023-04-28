import random
from .person_class import *
from .casino import *
from .card import *

TABLES = 1


class Table:
    table_counter = 0
    table_list = []
    table_name = f'Table {table_counter + 1}'

    def __init__(self, name, max_players=6, min_bet=2, max_bet=100, time_change=60):
        self.name = name
        self.max_players = max_players
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.time_change = time_change
        self.sitting = []
        self.shoe = []

    def __str__(self):
        return self.name

    def take_dealer(self):
        """
        Takes first or new dealer when needed
        """
        if self.sitting:
            curr_dealer = self.sitting[0].name
            self.sitting[0].playing = False
            Casino.shift.pop(Casino.occupied_dealers(curr_dealer))
            self.sitting.pop(0)
        else:
            dealer = random.choice(Casino.shift)
            self.sitting.append(dealer)
            Casino.occupied_dealers.append(dealer)
            dealer.playing = True
            Casino.shift.pop(Casino.shift.index(dealer))

    def imitate_player(self):
        """
        Adds NPCs to a table
        """
        for npc in NPC.NPC_list:
            if npc.playing:
                continue
            if self.max_players > len(self.sitting):
                self.sitting.append(npc)
                npc.playing = True

    @staticmethod
    def set_table():
        """
        Creates the required number of tables
        """
        for _ in range(TABLES):
            Table.table_counter += 1
            name = f'Table {Table.table_counter}'
            Table.table_list.append(Table(name))
        return

    def __iter__(self):
        return Iterator(self.sitting)

    def __getitem__(self, item):
        if item < 0 or item > 4:
            raise IndexError
        return self.shoe[item]

    def shuffle_cards(self):
        """
        Shuffles cards when needed
        """
        for _ in range(50):
            random.shuffle(self.shoe)

    def stop_card(self):
        """
        If during a deal of cards a dealer occurs this card. A dealer should finish the current deal.
        After having a deal finished a shoe should be renewed
        """
        card = 'card'
        self.shoe.insert(random.randint(-75, -65), card)

    def initial_deck(self):
        self.shoe.clear()
        for card in Card.card_list:
            self.shoe.append(card)
        self.shoe *= 6
        self.shuffle_cards()
        self.stop_card()

    def initial_hand(self):
        """
        Each player, NPC and dealer gets 2 cards
        """
        for _ in range(2):
            for player in self.sitting:
                if self.shoe[0] != 'card':
                    player.hand_list[0].append(self.shoe[0])
                    self.shoe.pop(0)
                else:
                    self.shoe.pop(0)
                    player.hand_list[0].append(self.shoe[0])
                    self.shoe.pop(0)

    def split(self):
        """
        After getting 2 cards as initial hand, each player and NPC can separate their cards if cards are equal
        """
        for player in self.sitting[1:]:
            if player.hand_list[0][0] == player.hand_list[0][1]:
                while True:
                    if player.ace_split != 0 and player.card_split != 0:
                        player.hand_list[3 - (player.card_split - 1)].append(player.hand_list[3 - player.card_split][1])
                        player.hand_list[3 - player.card_split].pop(1)
                        bet = list(player.bet_list[0])
                        player.bet_list[3 - (player.card_split - 1)] = bet
                        if 'card' not in (self.shoe[0], self.shoe[1]):
                            player.hand_list[3 - player.card_split].append(self.shoe[0])
                            player.hand_list[3 - (player.card_split - 1)].append(self.shoe[1])
                            self.shoe.pop(0)
                            self.shoe.pop(1)
                            if player.hand_list[3 - player.card_split][0][:-1] != 'a':
                                player.card_split -= 1
                                continue
                            else:
                                player.ace_split -= 1
                                break
                        else:
                            temp_value = self.shoe.index('card')
                            self.shoe.pop(temp_value)
                            continue
                    break

    def double_down(self):
        """
        Each player and NPC can double their bet if the total of their cards is in the range of 9-11
        """
        for player in self.sitting[1:]:
            i = 0
            for hand in player.hand_list:
                if hand:
                    if sum(e.value for e in hand) in (9, 10, 11):
                        player.bet_list[i][0] *= 2
                        if i < 3:
                            i += 1
                        else:
                            break


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration

