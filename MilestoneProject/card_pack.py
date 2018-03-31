import card
import random

class CardPack:

    __cards = []

    def __init__(self):
        self.init_cards()
    
    def __create_suite(self,suite):
        _suite = []

        _suite.append(card.Card("King",suite,10))
        _suite.append(card.Card("Queen",suite,10))
        _suite.append(card.Card("Jack",suite,10))
        _suite.append(card.Card("Ten",suite,10))
        _suite.append(card.Card("Nine",suite,9))
        _suite.append(card.Card("Eight",suite,8))
        _suite.append(card.Card("Seven",suite,7))
        _suite.append(card.Card("Six",suite,6))
        _suite.append(card.Card("Five",suite,5))
        _suite.append(card.Card("Four",suite,4))
        _suite.append(card.Card("Three",suite,3))
        _suite.append(card.Card("Two",suite,2))
        _suite.append(card.Card("Ace",suite,11,1))

        return _suite

    def init_cards(self):
        self.__cards.clear()

        self.__cards.extend(self.__create_suite("Spades"))
        self.__cards.extend(self.__create_suite("Hears"))
        self.__cards.extend(self.__create_suite("Diamonds"))
        self.__cards.extend(self.__create_suite("Clubs"))

    def reset_pack(self):
        self.init_cards()

    def get_all_cards(self):
        return self.__cards.copy()
    
    def take_card(self):
        if len(self.__cards) > 0:
            card_position = random.randrange(0,len(self.__cards))
            card = self.__cards[card_position]
            del self.__cards[card_position]
            return card
        else:
            return None