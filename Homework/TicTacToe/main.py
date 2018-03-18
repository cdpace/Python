import collections
import os

#global values
grid = [[0,0,0],[0,0,0],[0,0,0]]

#Initializes the players
def initPlayers():
    players = { 1: {}, 2: {}}
    symbols = ['X', 'O']
    choice = input("Player 1 what do you want to be X or O?: ").upper()

    if choice not in symbols:
        print('Option not available')
    else:
        name = input('Player 1 enter name: ')
        players[1] = { 'symbol' : choice, 'name': name }

        #remove chosen symbol to we can understand what the symbol of the other player will be
        symbols.remove(choice)

        name = input('Player 2 enter name: ')
        players[2] = { 'symbol': symbols[0], 'name': name}
    
    return players

#helper functions
def formatCol(colValue, colNumber):
    if colValue == 0:
        return f'({colNumber})'
    else:
        return f' {colValue} ' 

def drawGrid():
    print('|-----------|')
    colCounter = 0

    for row in grid:
        colnums = [0,0,0]

        for x in range(0,3):
            colCounter += 1
            colnums[x] = colCounter

        print(f'|{formatCol(row[0], colnums[0])}|{formatCol(row[1],colnums[1])}|{formatCol(row[2],colnums[2])}|')    
    
    print('|-----------|')

def setValueAndCheckWin(player, val):
    playerSymbol = player['symbol']

    if val in range(1,4):
        grid[0][val - 1] = playerSymbol
    elif val in range(4,7):
        grid[1][val - 4] = playerSymbol
    elif val in range(7,10):
        grid[2][val - 7] = playerSymbol
    
    #Check win condition
    for i in range(0,3):
        if grid[i].count(playerSymbol) == 3:
            return True
    
    

    return False

#Start the game
def start(players):
    player1 = players[1]
    player2 = players[2]

    currentPlayer = player1

    for turn in range(0,9):
        #show grid
        os.system('clear')

        drawGrid()
        #ask user for input
        if turn % 2 == 0:
            currentPlayer = player1
        else:
            currentPlayer = player2
        
        val = int(input('Turn({})-{}: '.format(turn + 1,currentPlayer['name'])))
        isWin = setValueAndCheckWin(currentPlayer, val)

        if isWin:
            os.system('clear')
            drawGrid()
            print(f'Congratulations {currentPlayer["name"]} you have won!!!')
            return True
    
    return False


#Main Run game
players = initPlayers()

#Start the game
someoneWon = start(players)

if someoneWon:
    print('Game Over')
else:
    print('Game Over, no player won')



