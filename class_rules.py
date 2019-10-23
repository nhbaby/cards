import pprint

class Rules():
    def __init__(self):
        return

    def winwin(self, player_info, community_card):
        for i, x in enumerate(player_info):
            # pprint.pprint(x)
            self.processing_card(x['hands'], community_card)
        return

    # 결과 판독
    def processing_card(self, cards, community_card):
        pprint.pprint("my hands~~~~~~")
        pprint.pprint(cards)
        # result_card = {'display': '', 'info': ''}

        # 191023 ###############################
        result_hands = {}
        for k, v in cards.items():
          if v[2] not in result_hands:
            result_hands[v[2]] = []

          result_hands[v[2]].append(v)

        pprint.pprint("result_hands !!!!!!!!!!!!!!!!!!")
        pprint.pprint(result_hands)

        # for idx, key in result_hands.items():
        #   print(idx, key)

        # 스트레이트 검사
        result_straight = []
        for key in sorted(result_hands, reverse=True):
          pprint.pprint("key : {0}".format(key))
          pprint.pprint(result_hands[key])

          if not result_straight:
            pprint.pprint("no straight!!!!!!!!")
            result_straight.append(result_hands[key])
          else:
            pprint.pprint("yes straight!!!!!!!!")
            prev_idx = len(result_straight) - 1
            pprint.pprint(result_straight)
            pprint.pprint("prev_idx : {}".format(prev_idx))
            pprint.pprint("value : {}".format(result_straight[prev_idx][0][2]))

            if result_straight[prev_idx][0][2] - 1 == result_hands[key][0][2]:
              
              result_straight.append(result_hands[key])
              pprint.pprint("continue straight!!!!!!!! : {}".format(len(result_straight)))
            else:
              pprint.pprint("stop straight!!!!!!!!")
              result_straight = []

        pprint.pprint("result_straight ```````````")
        pprint.pprint(result_straight)
        # for key, value in result_hands.items():
        #   pprint.pprint("key : {}".format(key))
        #   pprint.pprint("===> value : {}".format(value))


        ######################################

        # # 하이카드
        # high_card = 0
        # for c in cards:
        #     pprint.pprint(c)

        #     # A 때문에 여러개의 값을 확인함
        #     for n in c['values']:
        #         if n > high_card:
        #             high_card = n

        # pprint.pprint("------->>>  high card : {}".format(high_card))

        # result = {}
        # for c in cards:
        #     if not c['display'] in result:
        #         result[c['display']] = c

        # pprint.pprint("result ------------------")
        # pprint.pprint(result)
        # pprint.pprint(cards)


        # 원페어

        # 투페어

        # 셋

        # 스트레이트

        # 플러시

        # 풀하우스

        # 포카드

        # 스티플

        # 포티플

        return
