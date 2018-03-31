import card_pack
import game_service
import player
import os
import random

def printStatus(player_balance,cards, isDealer):
    print(f'Balance: €{player_balance} \n')

    hand_score = 0

    for card in cards:
        print(f'{card}')
        if len(card.values) > 1:
            if isDealer:
                hand_score += card.values[random.randint(0,1)]
            else:
                choice = int(f'Choose Value: (1){card.values[0]} - (2){card.values[1]}:') - 1
                hand_score += card.values[choice]
        else:
            hand_score += card.values[0]

    print(f'\n Hand Score: {hand_score}')


#Main Process
startingBalance = 500.00

print('Welcome to Chris BlackJack')

name = input('Enter your name: ')

client = player.Player(name,startingBalance)

print(f'{client.name} your account has been credit with €{startingBalance}')

service = game_service.GameService(client)

os.system('clear')

player_exit = False

dealer_cards = []
player_cards = []

while not player_exit and client.get_balance() > 0:
    
    dealer_cards.extend(service.deal_dealer_starting_hand())
    player_cards.extend(service.deal_player_starting_hand())

    print('Dealer:')
    printStatus(0, dealer_cards, True)

    print(f'{client.name}:')
    printStatus(client.get_balance(), player_cards, False)

    should_take_card = input('Take Cared (y/n): ').lower() == 'y'

    while should_take_card:
        player_cards.extend(service.player_take_card())

        os.system("clear")
        
        print('Dealer:')
        printStatus(0, dealer_cards, True)

        print(f'{client.name}:')
        printStatus(client.get_balance(), player_cards, False)

        
    

