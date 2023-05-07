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
        table.take_npc()
        table.initial_deck()

    for table in Table.table_list:
        table.initial_hand()
        table.bet()
        # table.split()
        # table.double_down()
        for player in table.sitting[1:]:
            for cards in player.hand_list:
                print(player.name, [e.name for e in cards], player.bet_list)


if __name__ == '__main__':
    main()

