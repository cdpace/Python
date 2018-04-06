import card_pack
import player as playerModel

class GameService:
    
    __playerPack = card_pack.CardPack()
    __dealerPack = card_pack.CardPack()
    

    def __init__ (self, player, win_percentage = 0.10):
        self.__player = player
        self.__win_percentage = win_percentage
    

    #public methods
    def deal_player_starting_hand(self):
        return self.__playerPack.take_cards(num = 2)
    

    def deal_dealer_starting_hand(self):
        cards_taken = self.__dealerPack.take_cards(num = 2)
        cards_taken[1].toggle_face()
        return cards_taken


    def player_take_card(self):
        cards = self.__playerPack.take_cards(num = 1)

        if len(cards) > 0:
            cards[0].toggle_face()
            return cards[0]
        else:
            return None
    

    def dealer_take_card(self):
        cards = self.__dealerPack.take_cards(num = 1)
        if(len(cards) > 0):
            cards[0].toggle_face()
            return cards[0]
        else:
            return None
    

    def is_bust(self, total_score):
        return total_score > 21
    

    def refresh(self):
        self.__playerPack.reset_pack()
        self.__dealerPack.reset_pack()
    

    def handle_player_win(self, stake):
        win_amount = stake + (self.__win_percentage * stake)
        self.__player.topup_balance(win_amount)
        return self.__player.get_balance()
    

    def handle_player_loss(self, stake):
        amount_left = self.__player.detuct_from_balance(stake)
        return amount_left <= 0
