import pprint

# 플레이어 세팅

class Player():

    # 플레이 가능한 최대 플레이어 수
    MAX_PLAYER_NUMBER = 10

    player_info = []

    def __init__(self, card_info):
        self.player_number = 0
        self.card_info = card_info
        return

    # 플레이어 지정
    def set_player(self, number):
        self.player_number = number

        if self.player_number > self.MAX_PLAYER_NUMBER:
            self.player_number = self.MAX_PLAYER_NUMBER

        for i in range(1, self.player_number + 1):
            # print("player : {}".format(i))

            player = {
                'name': i,
                'pos': None,
                'hands': {}
            }
            self.player_info.append(player)
            del player

        # print(self.player_info)

    # 카드 지급
    def get_card(self, put_card_number = 2):

        # 테스팅 위해서 카드 다중 지급용 로직!!
        for n in range(1, put_card_number + 1):
            for i, x in enumerate(self.player_info):

                user_card = self.card_info.pop_card()
                # print(user_card)
                # self.player_info[i]['hands'].append(self.card_info.pop_card())
                # self.player_info[i]['hands'][user_card['display']] = user_card
                self.player_info[i]['hands'][user_card[0]] = user_card

        # 카드 중복 지급 로직 필요함!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        pprint.pprint("self.player_info !!!!!!!!")
        pprint.pprint(self.player_info)

    def get_player_info(self):
        return self.player_info