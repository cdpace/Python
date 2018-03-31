import card_pack
import player as playerModel

class GameService:
    
    _playerPack = card_pack.CardPack()
    _dealerPack = card_pack.CardPack()
    
    def __init__ (self, player):
        self.__player = player
    

    #public methods
    def deal_starting_hand(self):
        pass
    

    def player_take_card(self):
        pass
    

    def dealer_take_card(self):
        pass
    


    #private methods
    
    
    