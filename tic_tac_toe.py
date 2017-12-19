#! python3

# tic tac toe program

import random


def pc_win(board,pc_inp,mapBoard):

    #row1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[1]]==pc_inp and board[mapBoard[2]]==' ') :
        board[mapBoard[2]]=pc_inp
        return 1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[2]]==pc_inp and board[mapBoard[1]]==' ') :
        board[mapBoard[1]]=pc_inp
        return 1
    if (board[mapBoard[2]]==pc_inp and board[mapBoard[1]]==pc_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1

    #row2
    if (board[mapBoard[0+3]]==pc_inp and board[mapBoard[1+3]]==pc_inp and board[mapBoard[2]+3]==' ') :
        board[mapBoard[2+3]]=pc_inp
        return 1
    if (board[mapBoard[0+3]]==pc_inp and board[mapBoard[2+3]]==pc_inp and board[mapBoard[1+3]]==' ') :
        board[mapBoard[1+3]]=pc_inp
        return 1
    if (board[mapBoard[2+3]]==pc_inp and board[mapBoard[1+3]]==pc_inp and board[mapBoard[0+3]]==' ') :
        board[mapBoard[0+3]]=pc_inp
        return 1

    
    #row3
    if (board[mapBoard[0+6]]==pc_inp and board[mapBoard[1+6]]==pc_inp and board[mapBoard[2+6]]==' ') :
        board[mapBoard[2+6]]=pc_inp
        return 1
    if (board[mapBoard[0+6]]==pc_inp and board[mapBoard[2+6]]==pc_inp and board[mapBoard[1+6]]==' ') :
        board[mapBoard[1+6]]=pc_inp
        return 1
    if (board[mapBoard[2+6]]==pc_inp and board[mapBoard[1+6]]==pc_inp and board[mapBoard[0+6]]==' ') :
        board[mapBoard[0+6]]=pc_inp
        return 1


    #column1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[3]]==pc_inp and board[mapBoard[6]]==' ') :
        board[mapBoard[6]]=pc_inp
        return 1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[6]]==pc_inp and board[mapBoard[3]]==' ') :
        board[mapBoard[3]]=pc_inp
        return 1
    if (board[mapBoard[6]]==pc_inp and board[mapBoard[3]]==pc_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1
    
    #column2
    if (board[mapBoard[0+1]]==pc_inp and board[mapBoard[3+1]]==pc_inp and board[mapBoard[6+1]]==' ') :
        board[mapBoard[6+1]]=pc_inp
        return 1
    if (board[mapBoard[0+1]]==pc_inp and board[mapBoard[6+1]]==pc_inp and board[mapBoard[3+1]]==' ') :
        board[mapBoard[3+1]]=pc_inp
        return 1
    if (board[mapBoard[6+1]]==pc_inp and board[mapBoard[3+1]]==pc_inp and board[mapBoard[0+1]]==' ') :
        board[mapBoard[0+1]]=pc_inp
        return 1

    #column3
    if (board[mapBoard[0+2]]==pc_inp and board[mapBoard[3+2]]==pc_inp and board[mapBoard[6+2]]==' ') :
        board[mapBoard[6+2]]=pc_inp
        return 1
    if (board[mapBoard[0+2]]==pc_inp and board[mapBoard[6+2]]==pc_inp and board[mapBoard[3+2]]==' ') :
        board[mapBoard[3+2]]=pc_inp
        return 1
    if (board[mapBoard[6+2]]==pc_inp and board[mapBoard[3+2]]==pc_inp and board[mapBoard[0+2]]==' ') :
        board[mapBoard[0+2]]=pc_inp
        return 1

    #diagonal1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[1*4]]==pc_inp and board[mapBoard[2*4]]==' ') :
        board[mapBoard[2*4]]=pc_inp
        return 1
    if (board[mapBoard[0]]==pc_inp and board[mapBoard[2*4]]==pc_inp and board[mapBoard[1*4]]==' ') :
        board[mapBoard[1*4]]=pc_inp
        return 1
    if (board[mapBoard[2*4]]==pc_inp and board[mapBoard[1*4]]==pc_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1
    
    #diagonal2
    if (board[mapBoard[4]]==pc_inp and board[mapBoard[6]]==pc_inp and board[mapBoard[2]]==' ') :
        board[mapBoard[2]]=pc_inp
        return 1
    if (board[mapBoard[4]]==pc_inp and board[mapBoard[2]]==pc_inp and board[mapBoard[6]]==' ') :
        board[mapBoard[6]]=pc_inp
        return 1
    if (board[mapBoard[2]]==pc_inp and board[mapBoard[6]]==pc_inp and board[mapBoard[4]]==' ') :
        board[mapBoard[4]]=pc_inp
        return 1

    return 0

def user_check(board,user_inp,pc_inp,mapBoard):

    #row1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[1]]==user_inp and board[mapBoard[2]]==' ') :
        board[mapBoard[2]]=pc_inp
        return 1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[2]]==user_inp and board[mapBoard[1]]==' ') :
        board[mapBoard[1]]=pc_inp
        return 1
    if (board[mapBoard[2]]==user_inp and board[mapBoard[1]]==user_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1

    #row2
    if (board[mapBoard[0+3]]==user_inp and board[mapBoard[1+3]]==user_inp and board[mapBoard[2+3]]==' ') :
        board[mapBoard[2+3]]=pc_inp
        return 1
    if (board[mapBoard[0+3]]==user_inp and board[mapBoard[2+3]]==user_inp and board[mapBoard[1+3]]==' ') :
        board[mapBoard[1+3]]=pc_inp
        return 1
    if (board[mapBoard[2+3]]==user_inp and board[mapBoard[1+3]]==user_inp and board[mapBoard[0+3]]==' ') :
        board[mapBoard[0+3]]=pc_inp
        return 1

    
    #row3
    if (board[mapBoard[0+6]]==user_inp and board[mapBoard[1+6]]==user_inp and board[mapBoard[2+6]]==' ') :
        board[mapBoard[2+6]]=pc_inp
        return 1
    if (board[mapBoard[0+6]]==user_inp and board[mapBoard[2+6]]==user_inp and board[mapBoard[1+6]]==' ') :
        board[mapBoard[1+6]]=pc_inp
        return 1
    if (board[mapBoard[2+6]]==user_inp and board[mapBoard[1+6]]==user_inp and board[mapBoard[0+6]]==' ') :
        board[mapBoard[0+6]]=pc_inp
        return 1


    #column1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[3]]==user_inp and board[mapBoard[6]]==' ') :
        board[mapBoard[6]]=pc_inp
        return 1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[6]]==user_inp and board[mapBoard[3]]==' ') :
        board[mapBoard[3]]=pc_inp
        return 1
    if (board[mapBoard[6]]==user_inp and board[mapBoard[3]]==user_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1
    
    #column2
    if (board[mapBoard[0+1]]==user_inp and board[mapBoard[3+1]]==user_inp and board[mapBoard[6+1]]==' ') :
        board[mapBoard[6+1]]=pc_inp
        return 1
    if (board[mapBoard[0+1]]==user_inp and board[mapBoard[6+1]]==user_inp and board[mapBoard[3+1]]==' ') :
        board[mapBoard[3+1]]=pc_inp
        return 1
    if (board[mapBoard[6+1]]==user_inp and board[mapBoard[3+1]]==user_inp and board[mapBoard[0+1]]==' ') :
        board[mapBoard[0+1]]=pc_inp
        return 1

    #column3
    if (board[mapBoard[0+2]]==user_inp and board[mapBoard[3+2]]==user_inp and board[mapBoard[6+2]]==' ') :
        board[mapBoard[6+2]]=pc_inp
        return 1
    if (board[mapBoard[0+2]]==user_inp and board[mapBoard[6+2]]==user_inp and board[mapBoard[3+2]]==' ') :
        board[mapBoard[3+2]]=pc_inp
        return 1
    if (board[mapBoard[6+2]]==user_inp and board[mapBoard[3+2]]==user_inp and board[mapBoard[0+2]]==' ') :
        board[mapBoard[0+2]]=pc_inp
        return 1

    #diagonal1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[1*4]]==user_inp and board[mapBoard[2*4]]==' ') :
        board[mapBoard[2*4]]=pc_inp
        return 1
    if (board[mapBoard[0]]==user_inp and board[mapBoard[2*4]]==user_inp and board[mapBoard[1*4]]==' ') :
        board[mapBoard[1*4]]=pc_inp
        return 1
    if (board[mapBoard[2*4]]==user_inp and board[mapBoard[1*4]]==user_inp and board[mapBoard[0]]==' ') :
        board[mapBoard[0]]=pc_inp
        return 1
    
    #diagonal2
    if (board[mapBoard[4]]==user_inp and board[mapBoard[6]]==user_inp and board[mapBoard[2]]==' ') :
        board[mapBoard[2]]=pc_inp
        return 1
    if (board[mapBoard[4]]==user_inp and board[mapBoard[2]]==user_inp and board[mapBoard[6]]==' ') :
        board[mapBoard[6]]=pc_inp
        return 1
    if (board[mapBoard[2]]==user_inp and board[mapBoard[6]]==user_inp and board[mapBoard[4]]==' ') :
        board[mapBoard[4]]=pc_inp
        return 1

    return 0


def pc_logical_move(ran_num,user_inp_move,board,mapBoard):
    global case
    logical_move_value=-1
    user_move_int=-1
    for k in mapBoard:
        if user_inp_move==mapBoard[k]:
            user_move_int=k        
    
    if (ran_num in [0,2,8,6] and user_move_int in [0,2,6,8]) or (case==1):
        case=1
        while True:
            logical_move_value=random.choice([0,2,6,8])
            if board[mapBoard[logical_move_value]] != ' ':
                 continue
            else:
                break
            
    elif (ran_num in [0,2,8,6] and user_move_int in [1,3,5,7]) or (case==2):
        check=-1
        if case!=2:
            if (ran_num-6)>=0:
                check=ran_num-6
                if board[mapBoard[ran_num-3]] != ' ':
                    if ran_num==8:
                        logical_move_value=6
                    else:
                        logical_move_value=8
                else:
                    logical_move_value=check
            else:
                check=ran_num+6
                if board[mapBoard[ran_num+3]] != ' ':
                    if ran_num==0:
                        logical_move_value=2
                    else:
                        logical_move_value=0
                else:
                    logical_move_value=check
        else:
            logical_move_value=4
        case=2

    elif (ran_num in [0,2,6,8] and user_move_int in[4]) or (case==3):
        case=3
        while True:
            logical_move_value=random.choice([0,1,2,3,4,5,6,7,8])
            if board[mapBoard[logical_move_value]] != ' ':
                 continue
            else:
                break
    return logical_move_value
        



def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-----')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-----')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])








# asking user for X or O
print('Welcome to tic tac toe!\nDo you want to be X or O ?')
user_inp=input()
user_inp=user_inp.upper()
pc_inp=' '
if user_inp=='X':
    pc_inp='O'
else:
    pc_inp='X'

print('The computer will go first.')

theBoard={'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ', 'low-R':' ' }

mapBoard={0:'top-L', 1:'top-M', 2:'top-R', 3:'mid-L', 4:'mid-M', 5:'mid-R', 6:'low-L', 7:'low-M', 8:'low-R' }

case=-1
#printBoard(theBoard)
pc_win_output=0

ran_num= random.choice([0,2,6,8])
theBoard[mapBoard[ran_num]]=pc_inp
printBoard(theBoard)

user_inp_move=' '
pc_win_output=0
user_check_output=0
i=4
game_check=0
while i>0:
    print('What is your next move? (top-, mid-, low-, & L, M, R)')
    user_inp_move=input()

    while True:
        if user_inp_move not in theBoard.keys() or theBoard[user_inp_move]!=' ':
            print('enter the valid place')
        else:
            break
        user_inp_move=input()

    theBoard[user_inp_move]=user_inp
    #printBoard(theBoard)
    pc_win_output=pc_win(theBoard,pc_inp,mapBoard)
    if pc_win_output:
        printBoard(theBoard)
        print('PC won the game')
        game_check=1
        break
    else:
        user_check_output=user_check(theBoard,user_inp,pc_inp,mapBoard)
        if user_check_output==0:
            ran_num= pc_logical_move(ran_num,user_inp_move,theBoard,mapBoard)
            theBoard[mapBoard[ran_num]]=pc_inp
        printBoard(theBoard)
    i-=1
        
if game_check==0:
    print('It is a draw. lol . You cannot defeat me')



    
