from classes.table_class import *
from classes.person_class import *


def main():
    NPC.gen_npc()
    Dealer.gen_dealer()
    Table.set_table()
    Dealer.imitate_shift()
    Card.set_value()
    for table in Table.table_list:
        table.take_dealer()
        table.imitate_player()
        table.initial_deck()
    for table in Table.table_list:
        table.initial_hand()
        for player in table.sitting[1:]:
            player.bet()
    for table in Table.table_list:
        table.split()
        table.double_down()
        for player in table:
            for cards in player.hand_list:
                print(player.name, player.bet_list, [e.name for e in cards], sum([e.value for e in cards]))


if __name__ == '__main__':
    main()

