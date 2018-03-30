import card_pack
import player as playerModel

class GameService:
    
    __pack = card_pack.CardPack()
    
    def __init__ (self, player):
        self.__player = player
    
    