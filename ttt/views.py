
from typing import Dict, List, Any
import sys,random
import time, copy
import argparse
from venv import create
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from random import choice
import platform
import time
from os import system





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
    response=''

    for foo in board:
        for oof in foo:
            response+=oof
    return response



def getMove(board):


    convertBoard(board)
    
    printBoard(board)
    makeMove(board)
    printBoard(board)

    convertBackBoard(board)



#evaluation of state.
#takes current board
#returns +1 if computer wins -1 if human wins 0 if drawn
def evaluate(state):
    H = -1
    C = +1

    if wins(state, C):
        score = 1
    elif wins(state, H):
        score = -1
    else:
        score = 0

    return score

#takes state of current board and player human or computer
#returns true if the player has won
def wins(state, player):

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


#check if board is in terminal state by winner
def game_over(state):
    H = -1
    C = +1
    return wins(state, H) or wins(state, C)



#takes board state
#returns list of cordinates for each empty cell
def possibleMoves(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells



#takes board state current depth and current player
#calls it self recursively until at terminal state or max depth
#then returns cordinates of best move with score.
def recursion(state, depth, player):
    H = -1
    C = +1

    if player == 1:
        best = [-1, -1, -1000]##max value
    else:
        best = [-1, -1, +1000]##min value

        
    if depth == 0 or game_over(state):
        score = evaluate(state)#set new score
        return [-1, -1, score]#returns final score, this final node
    for move in possibleMoves(state):#iterates possible move
        x, y = move[0], move[1]
        state[x][y] = player
        score = recursion(state, depth - 1, -player)
        
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == C:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best



#starts recursion if not in terminal state
#when recursion is finished board is updated
def makeMove(board):
    H = -1
    C = +1

    depth = len(possibleMoves(board))
    if depth == 0 or game_over(board):#if in terminal state
        return

    move = recursion(board, depth, C)#get move from minimax
    x, y = move[0], move[1] ##set xy cords
    board[x][y] = 1##make move 1 for o

##converts board to 1,0,-1 from o,_,x
def convertBoard(board):
    for foo in range(len(board)):
        for oof in range(len(board[foo])):
            if board[foo][oof] == 'x':
                board[foo][oof] = -1
            if board[foo][oof] == 'o':
                board[foo][oof] = 1
            if board[foo][oof] == '_':
                board[foo][oof] = 0
            if board[foo][oof] == '-':
                board[foo][oof] = 0

##converts board to o,_,x from 1,0,-1
def convertBackBoard(board):
    for foo in range(len(board)):
        for oof in range(len(board)):
            if board[foo][oof] == -1:
                board[foo][oof] = 'x'
            if board[foo][oof] == 1:
                board[foo][oof] = 'o'
            if board[foo][oof] == 0:
                board[foo][oof] = '_'

##check winner give board with x_o
##returns string x o or _ depending on winner
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


#makes random move of o
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

#check if board is full returns true/false
def checkFull(board):
    found = False
    for foo in board:
        for oof in foo:
            if oof =='_':
                found=True
    return found
#updates the board given a string from url
def updateBoard(board, url):
    count = 0
    for foo in range(0,3):
        for oof in range(0,3):
            board[foo][oof]=url[count]
            count+=1
#creates a 3 x 3 array with each index inialized to _
def createBoard(board):
    for foo in range(0,3):
        board.append([])
        for oof in range(0,3):
            board[foo].append('-')

#prints board in lines
def printBoard(board):
    for line in board:
        print(line)

