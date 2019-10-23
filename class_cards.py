import random
import pprint
import sys

class Cards:
  def __init__(self):

    # 카드 정의
    # dict
    # spec_cards = {}

    # list
    self.spec_cards = []
    self.shape_cards = ['s', 'd', 'h', 'c']
    self.display_cards = {
      11 : 'J',
      12 : 'Q',
      13 : 'K',
      14 : 'A'
    }

    for s in self.shape_cards:
      for n in range(2, 15):
        # print("{} - {}".format(s, n))

        display_name = "{}{}".format(s, self.display_cards[n] if n in self.display_cards else n)
        number = n

        # if n == 1:
        #   number.append(14)

        # number 높은 숫자로 정렬이 필요할까?

        # card = {
        #   "display": display_name,
        #   "shape": s,
        #   "values": number
        # }

        card = (display_name, s, number)

        # dict
        # spec_cards[display_name] = card

        # list
        self.spec_cards.append(card)
        del card

    # 카드 세팅 잘 됐는지 검증 필요함!!!!

    ###### dict ###########
    # # print(spec_cards)
    # keys = list(spec_cards.keys())
    # # print(keys)

    # l = list(spec_cards.items())
    # random.shuffle(l)
    # random_cards = dict(l)
    # print(random_cards)
    # print(len(random_cards))

    # def pop_card(cards):
    #   for key, value in cards.items():
    #     return (key, value)
    # for i in range(1, 10):
    #   print(pop_card(random_cards))

    # pprint.pprint("setting !!!!!!!!!!!!!!")
    # pprint.pprint(self.spec_cards)
    # sys.exit()
    return




  def random_cards(self):
    ######## list ##############
    random.shuffle(self.spec_cards)

    # pprint.pprint("shuffle ~~~~~~~~~~~~")
    # pprint.pprint(self.spec_cards)
    # pprint.pprint(len(self.spec_cards))
    # sys.exit()
    return

  def pop_card(self):
    return self.spec_cards.pop()
      # for key, value in cards.items():
      #   return (key, value)

  def test(self):
    for i in range(1, 10):
      print("^"*10)
      print(self.pop_card())
      print(len(self.spec_cards))