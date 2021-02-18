
from IPython.display import clear_output

#funtion to print board
def display_board(board):
    print('|   |   |   |')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('|___|___|___|')
    print('|   |   |   |')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('|___|___|___|')
    print('|   |   |   |')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print('|   |   |   |')
    pass

#take in a player input and assign their marker as 'X' or 'O'
def player_input():
    
    markers = ['X','O']
    
    marker = ''
    
    while marker not in markers:
        marker = input ("Player 1, choose X or O:")
        player1 = marker
        
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    
    return(player1,player2)

    #takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
    def place_marker(board, marker, position):
    
    #board = ['#','','','','','','','','','']
    board[pos] = marker

# takes in a board and a marker(X or O) and checks for a winner
def win_check(board, mark):
    
    return ((board[1] == board[2] == board[3] == mark) or #bottom
            (board[4] == board[5] == board[6] == mark) or #middle
            (board[7] == board[8] == board[9] == mark) or #top
            
            (board[1] == board[4] == board[7] == mark) or #left
            (board[2] == board[5] == board[8] == mark) or #middle
            (board[3] == board[6] == board[9] == mark) or #right
            
            (board[1] == board[5] == board[9] == mark) or #diagonals
            (board[3] == board[5] == board[7] == mark))

#pick which player starts

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#check if space free on board and returns a boolean value.    
def space_check(board, pos):
    return board[pos] == ' '
    
#checks if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#asks for a player's next position (as a number 1-9) 
def player_choice(board):
    
    pos = 0
    
    acceptable_pos = [1,2,3,4,5,6,7,8,9]
    
    while pos not in acceptable_pos or not space_check(board, pos):
        pos = int(input('Choose a position (as a number 1-9): '))
        
        
            
    return pos

#asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    
    acceptable_responses = ['y','n']
    
    choice = 'wrong'
    
    while choice not in acceptable_responses and not game_on:
        choice = input ("Do you want to start playing again? ( Enter y or n) : ")
        
        if choice not in acceptable_responses:
            print("Please choose y or n")
            
        if choice == "y":
            return True
        else: return False


#gameplay
print('Welcome to Noughts and Crosses!')

while True:
    board = [' '] * 10 #board list
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first')
    
    play_game = input('Are you ready to play? y or n: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            
            #Player 1 Turn
            display_board(board)
            pos = player_choice(board)
            place_marker(board, player1_marker, pos)
            
            #wincheck
            if win_check(board, player1_marker):
                display_board(board)
                print('Congrats player 1, you won!')
                game_on = False
                
            #full check
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                
                #change turn
                else:
                     turn = 'Player 2'
                          
                
        # Player2's turn.
        
            display_board(board)
            pos = player_choice(board)
            place_marker(board, player2_marker, pos)
            
            #wincheck
            if win_check(board, player2_marker):
                display_board(board)
                print('Congrats player 2, you won!')
                game_on = False
                
            #full check
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw')
                    break
                
                #change turn
                else:
                     turn = 'Player 1'
            
            
    if not replay():
        break