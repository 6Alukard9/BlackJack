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
        self.temp_shoe = self.gen_shoe_iterator()
        self.stop_card_found = False

    def __str__(self):
        return self.name

    def __iter__(self):
        return Iterator(self.sitting)

    def __getitem__(self, item):
        if item < 0 or item > len(self.shoe):
            raise IndexError
        return self.shoe[item]

    def take_dealer(self):
        """
        Takes first or new dealer when needed
        """

        dealer = random.choice(Casino.shift)
        self.sitting.append(dealer)
        Casino.occupied_dealers.append(dealer)
        dealer.playing = True
        Casino.shift.pop(Casino.shift.index(dealer))

    def take_npc(self):
        """
        Adds NPCs to a table
        """
        for npc in NPC.NPC_list:
            npc.t_name = self.name
            if npc.playing:
                continue
            if self.max_players > len(self.sitting):
                self.sitting.append(npc)
                npc.playing = True

    def bet(self):
        """
        Returns random bet in the range of 2-100
        """
        for player in self.sitting[1:]:
            player.bet_list[0].append(random.randint(2, 100))

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

    def shuffle_cards(self):
        """
        Shuffles cards when needed
        """

        for _ in range(20):
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

    def gen_shoe_iterator(self):
        if 'card' in self.shoe:
            self.shoe.remove('card')
        self.shuffle_cards()
        self.stop_card()

        for card in self.shoe:
            yield card

    def initial_hand(self):
        """
        Each player, NPC and dealer gets 2 cards
        """

        for _ in range(2):
            for player in self.sitting:
                temp_value = next(self.temp_shoe)
                if temp_value != 'card':
                    player.hand_list[0].append(temp_value)
                else:
                    self.stop_card_found = True
                    player.hand_list[0].append(next(self.temp_shoe))

    def split(self):
        """
        After getting 2 cards as initial hand, each player and NPC can separate their cards if cards are equal
        """
        def grf():
            count_hand = -1
            for cards in player.hand_list:
                count_hand += 1
                if cards:
                    if cards[0] == cards[1]:
                        if player.ace_split != 0 and player.card_split != 0:
                            player.hand_list[3 - (player.card_split - 1)].append(player.hand_list[count_hand][1])
                            player.hand_list[count_hand].pop(1)
                            bet = player.bet_list[0]
                            player.bet_list[3 - (player.card_split - 1)] = bet

                            temp_value = next(self.temp_shoe)
                            temp_value2 = next(self.temp_shoe)
                            if 'card' not in (temp_value, temp_value2):
                                player.hand_list[count_hand].append(temp_value)
                                player.hand_list[3 - (player.card_split - 1)].append(temp_value2)
                                if player.hand_list[3 - (player.card_split - 1)][0][:-1] != 'a' \
                                        and player.hand_list[count_hand][0][:-1]:
                                    player.card_split -= 1
                                else:
                                    player.ace_split -= 1
                                    break
                            else:
                                if temp_value == 'card':
                                    print('!!!!!!!!!!!!!!!!')
                                    temp_value = next(self.temp_shoe)
                                elif temp_value2:
                                    print('AAAAAAAAAAAAAAAAA')
                                    temp_value2 = next(self.temp_shoe)
                                continue

                            break

        for player in self.sitting[1:]:
            grf()

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

