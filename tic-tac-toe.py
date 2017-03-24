


from random import randint 

def initialise_board(board_size):
      board= [ [ "-" for y in range(board_size) ] for x in range(board_size) ]
      return board
               
def winning_row(test_list,blankchar):
    x= test_list[0]
    for i in range(len(test_list)):
        if x != test_list[i] or x== blankchar:
            return 0
    return 1

def check_win(board,board_length,blankchar):
    diagonal= []
    for i in range(board_length):
        diagonal.append(board[i][i])        
        if winning_row(board[i],blankchar):
            return 1
        test_row= []
        for j in range(board_length):
            test_row.append(board[j][i])
        if winning_row(test_row,blankchar):
            return 1
    if winning_row(diagonal,blankchar):
        return 1
    return 0
    
def print_board(board):
      divider= [""]
      for i in range(3):
            divider.append("---")
      print("".join(divider))
      for row in board:
          print(" | ".join(row))
          print("".join(divider))
          
def getinput(board,inputframe):
    while True:
        try:
            print_board(board)
            print('Use the numpad for your move!')
#            print_board(inputframe)
            move= int(input('Your move (1-9): '))
            if move >0 and move <=10:
                return move
                break
            else:
                print('Between 1 and 9, please!')
        except ValueError:
            print("Oops!  I didn't understand.  Try again...")

def fillboard(board,place,player):
    markers= ['o','x']
    row= [2,2,2,1,1,1,0,0,0]
    col= [0,1,2,0,1,2,0,1,2]
    print(player)
    board[row[place-1]][col[place-1]]= markers[player]
    return board
          
def check_spot(board,place,blankchar):
    row= [2,2,2,1,1,1,0,0,0]
    col= [0,1,2,0,1,2,0,1,2]
    if board[row[place-1]][col[place-1]] == blankchar:
        return 1
    return 0
    
def get_move(board,inputframe,blankchar):
    while True:
        try:
            move=getinput(board,inputframe)
            if check_spot(board,move,blankchar):
                return move
                break
            else:
                print("That spot's already taken!")
        except ValueError:
            print("Oops!  I didn't understand.  Try again...")
            
board= initialise_board(3)
inputframe= [['7','8','9'],['4','5','6'],['1','2','3']]
counter=1

while True:
    if counter%2:
        move= get_move(board,inputframe,"-")
    else:
        while True:
            move= randint(1,9)
            if check_spot(board,move,"-"):
                break
    board= fillboard(board,move,counter%2)
    counter+= 1
    if check_win(board,3,"-"):
        print("Game's over!")
        print_board(board)
        break