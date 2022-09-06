
from typing import Dict, List, Any
import sys,random
import time, copy
import argparse
from venv import create
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse




def index(request):
    context = {}
    return render(request, 'ttt/index.html',context)


def move(request):

    url = request.build_absolute_uri()
    url = url.split('asdf=')[1]

    #print(url)

    board = createBoard()
    board = updateBoard(board, url)
    #printBoard(board)

    board =  getMove(board)
    r = getResponse(board)
    winner = won(board)

    #print(r)




    return JsonResponse({'asdf': r,'winner':winner})
 
def getResponse(board):
    response=''

    for foo in board:
        for oof in foo:
            response+=oof
    return response



def getMove(board):
    
    randMove(board)
   
    #board = test(board)


    return board





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

    return board

def createBoard():

    board = []

    
    for foo in range(0,3):
        board.append([])
        for oof in range(0,3):
            board[foo].append('-')

    return board



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