
from typing import Dict, List, Any
import sys,random
import time, copy
import argparse
from venv import create
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from math import inf as infinity
from random import choice
import platform
import time
from os import system




HUMAN = -1
COMP = +1


def index(request):
    context = {}
    return render(request, 'ttt/index.html',context)


def move(request):

    url = request.build_absolute_uri()
    url = url.split('asdf=')[1]

    #print(url)
    

    board = []

    createBoard(board)
    updateBoard(board,url)

    getMove(board)
    r = getResponse(board)
    winner = won(board)
    if checkFull(board) == False and winner!='x' and winner!= 'o':
        winner = 't'





    return JsonResponse({'asdf': r,'winner':winner})
 
def getResponse(board):
    convertBackBoard(board)
    printBoard(board)
    response=''

    for foo in board:
        for oof in foo:
            response+=oof
    return response



def getMove(board):
    
    convertBoard(board)
    print('asdf')
    printBoard(board)



    ai_turn('o', 'x',board)
    print(board)








def convertBoard(board):
    for foo in range(len(board)):
        for oof in range(len(board[foo])):
            if board[foo][oof] == 'x':
                board[foo][oof] = -1
            if board[foo][oof] == 'o':
                board[foo][oof] = 1
                print(board[foo][oof])
            if board[foo][oof] == '_':
                board[foo][oof] = 0
            if board[foo][oof] == '-':
                board[foo][oof] = 0


def convertBackBoard(board):
    print(board)
    for foo in range(len(board)):
        for oof in range(len(board)):
            if board[foo][oof] == -1:
                board[foo][oof] = 'x'
            if board[foo][oof] == 1:
                board[foo][oof] = 'o'
                print(board[foo][oof])
            if board[foo][oof] == 0:
                board[foo][oof] = '_'



def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y, board):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player,board):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y,board):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player,board):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(board):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player,board)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean1():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render1(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice,board):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean1()
    print(f'Computer turn [{c_choice}]')
    render1(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP,board)
        x, y = move[0], move[1]

    set_move(x, y, COMP,board)
    time.sleep(1)

def test(depth,board,best,root):

    if depth % 2 != 0:
        team ='x'
        score = -10000

    else:
        team = 'o'
        score = 10000
    if depth > 0 and won(board) == None and checkFull(board):


        if depth == 99:
            print('#########################')
            print(best)
            printBoard(best[1])
            root = board

        moves = possibleMoves(board,team)
        for move in moves:
            #printBoard(move)
            test(depth-1,move,best,root)
    elif won(board) == 'x':
        score -=100
    elif won(board) == 'o':
        score +=10
    if score >best[0]:
        best[0] = score
        best[1] = root
        print('updated')
    return best
    


def fn(depth,board):
    score=evaluate(board)
    if depth >0:
        moves = possibleMoves(board,'o')
        for move in moves:
            printBoard(move)
            score = fn(depth-1,move)



    return score




def possibleMoves(board,team):
    counter = 0
    moves = []
    for foo in range(0,3):
        for oof in range(0,3):
            if(board[foo][oof]=='_'):
                x = copy.deepcopy(board)
                x[foo][oof]=team
                moves.append(x)
                counter+=1
                
    return moves
    

'''
def evaluate(board):

    if won(board)=='o':
        score = +1
    elif won(board)=='x':
        score = -1
    else:
        score = 0

    return score
'''

def won(board):
    winner = '_'
    #horizontal
    teams = ['x','o']
    for team in teams:
        c=0
        for foo in board:
            c+=1
            count =0
            for oof in foo:
                if oof == team:
                    count+=1

            if count == 3:
                return team

    #vertical
    teams = ['x','o']
    for team in teams:
        for foo in range(0,3):
            count =0
            for oof in range(0,3):
                if board[oof][foo] == team:
                        count+=1
            if count == 3:
                return team
    #diagonal
    teams = ['x','o']
    for team in teams:
        if board[0][0]==team and board[1][1]==team and board[2][2]==team:
            return team
        if board[2][0]==team and board[1][1]==team and board[0][2]==team:
            
            return team





def randMove(board):
    if checkFull(board):
        searching = True
        while searching:
            num1 = random.randint(0, 2)
            num2 = random.randint(0, 2)
            print(num1,num2)
            if(board[num1][num2]=='_'):
                searching = False
                board[num1][num2]='o'


    return board
def checkFull(board):
    found = False
    for foo in board:
        for oof in foo:
            if oof =='_':
                found=True

    return found

def updateBoard(board, url):
    count = 0
    for foo in range(0,3):
        for oof in range(0,3):
            board[foo][oof]=url[count]
            count+=1


def createBoard(board):

    for foo in range(0,3):
        board.append([])
        for oof in range(0,3):
            board[foo].append('-')




def printBoard(board):
    for line in board:
        print(line)






'''
def test(board):

    ###

    ###moves {1 : {move: baord, pissibleMoves : { ... }}}


    moves = possibleMoves(board,'o')
    moves = getNext(moves)
    moves = removeL(moves)
    remove_(moves)
    for move in moves:
        printBoard(moves[move]['move'])
        board = moves[move]['move']
    #for move3 in moves[move]['possibleMoves'][move2]['possibleMoves']:
    #printBoard(moves[0]['possibleMoves'][0]['possibleMoves'][0]['move'])


    #print(moves)


    #board = randMove(board)
    return board



def remove_(moves):
    finalMoves = copy.deepcopy(moves)



    
    return finalMoves

def removeL(moves):
    finalMoves = copy.deepcopy(moves)
    for move in moves:
        winner = won(moves[move]['move'])
        if winner == 'x':
            print(winner)
            finalMoves.pop(move,None)
        for move2 in moves[move]['possibleMoves']:
            winner = won(moves[move]['possibleMoves'][move2]['move'])
            if winner == 'x':
                print(winner)
                finalMoves.pop(move,None)
            for move3 in moves[move]['possibleMoves'][move2]['possibleMoves']:
                winner = won(moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['move'])
                if winner == 'x':
                    try:
                        finalMoves.pop(move,None)
                    except KeyError:
                        print('already removed  ')
                    
                for move4 in moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['possibleMoves']:
                        winner = won(moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['possibleMoves'][move4]['move'])
                        if winner == 'x':
                            print(winner)
                            try:
                                finalMoves.pop(move,None)
                            except KeyError:
                                print('already removed  ')


    return finalMoves



def getNext(moves):
    
    for move in moves:
        currentMove = moves[move]['move']
        moves[move]['possibleMoves'].update(possibleMoves(currentMove,'x'))

        for move2 in moves[move]['possibleMoves']:
            currentMove2 = moves[move]['possibleMoves'][move2]['move']
            moves[move]['possibleMoves'][move2]['possibleMoves'].update(possibleMoves(currentMove2,'o'))
            for move3 in moves[move]['possibleMoves'][move2]['possibleMoves']:
                moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['possibleMoves'].update(possibleMoves(currentMove2,'x'))
                for move4 in moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['possibleMoves']:
                    moves[move]['possibleMoves'][move2]['possibleMoves'][move3]['possibleMoves'][move4]['possibleMoves'].update(possibleMoves(currentMove2,'x'))

    return moves
    


def possibleMoves(board,team):
    moves = {}
    counter = 0
    for foo in range(0,3):
        for oof in range(0,3):
            if(board[foo][oof]=='_'):
                x = copy.deepcopy(board)
                x[foo][oof]=team
                moves.update({counter: {'move':x,'possibleMoves':{}}})
                counter+=1
                
                
    return moves

'''