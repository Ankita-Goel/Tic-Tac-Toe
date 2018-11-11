from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
def player_input():
    marker=''
    
    # keep asking player 1 to choose X or O
    
    while marker != 'X' and marker !='O':
        marker= input('Player 1: Please choose X or O:').upper()
        
    # assign player 2 opposite marker
    player1= marker
    if player1 =='X':
        player2 ='O'
    else:
        player2 ='X'
    
    return(player1,player2)

def place_marker(board,marker,position):
    board[position]= marker
    
def win_check(board,mark):
    
    return((board[1] == board[2] == board[3] ==mark) or (board[4] == board[5] == board[6] ==mark) or
           (board[7] == board[8] == board[9] ==mark) or (board[1] == board[4] == board[7] ==mark) or
           (board[2] == board[5] == board[8] ==mark) or (board[3] == board[6] == board[9] ==mark) or
           (board[1] == board[5] == board[9] ==mark) or (board[3] == board[5] == board[7] ==mark))

def choose_first():
    
    flip=random.randint(0,1)
    
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

def check_space(board,position):
    
    return board[position]== ' '

def check_full(board):
    
    for i in range(1,10):
        if check_space(board,i):
            return False
    
    # if board is full
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) or not check_space(board,position):
        position= int(input('Choose a position (1-9):'))

    return position

def replay():
    
    choice= input('Want to play again? Yes or No')
    return choice =='Yes'


    
# while loop to keep running the game

print('Welcome to Tic Tac Toe!')

while True:
    
    the_board= [' ']*10
    player1_marker, player2_marker= player_input()
    
    turn= choose_first()
    print(turn + ' will go first.\n')
    
    start= input('\nAre you ready to play? Enter Yes or No: ')
    if start=='Yes':
        game_on= True
    else: 
        game_on =False
        
    # game play
    
    while game_on:
        
        if turn =='Player 1':
           	 # player 1 turn
            
           	 #show the board
            display_board(the_board)
            print('player 1 turn:')
           	 #choose a position
            position = player_choice(the_board)
            
            	#place the marker on the position
            place_marker(the_board,player1_marker,position)
            
           	 #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!!')
                game_on= False
            else:
            	# check if there is a tie
                if check_full(the_board):
                    display_board(the_board)
                    print('TIE GAME!!!!')
                    game_on= False
                else:
                    turn= 'Player 2'
            
        else:
           	 # player 2 turn
            
           	 #show the board
            display_board(the_board)
            
           	 #choose a position
            position = player_choice(the_board)
            print('player 2 turn')
            
           	 #place the marker on the position
            place_marker(the_board,player2_marker,position)
            
           	 #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!!')
                game_on= False
            else:
          	  # check if there is a tie
                if check_full(the_board):
                    display_board(the_board)
                    print('TIE GAME!!!!')
                    game_on= False
                else:
                    turn= 'Player 1'
    if not replay():
        break
        
    # break out of the while loop on replay()