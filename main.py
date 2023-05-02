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
        table_name = Table.table_list.index(table.name)
        for player in table.sitting[1:]:
            player.split(table_name)
            player.double_down()
            for cards in player.hand_list:
                print([e.name for e in cards])
                # for card in cards:
                #     print(card.name, card.value, f'{id(card): ,}')


if __name__ == '__main__':
    main()

