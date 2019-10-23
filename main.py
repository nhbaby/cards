import class_cards
import class_users
import class_rules

import sys

# 플레이어 수
player_number = 3
put_card_number = 15

sc = class_cards.Cards()
# sys.exit()
sc.random_cards()
# sc.test()




players = class_users.Player(sc)
players.set_player(player_number)
players.get_card(put_card_number)
# sys.exit()

community_card = []

rules = class_rules.Rules()
# print(players.get_player_info())
# sys.exit()
rules.winwin(players.get_player_info(), community_card)