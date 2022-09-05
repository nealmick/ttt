
from typing import Dict, List, Any
import sys,random
import time
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

    print(url)

    board = createBoard()
    board = updateBoard(board, url)
    board =  getMove(board)
    printBoard(board)
    r = getResponse(board)
    print(r)




    return JsonResponse({'asdf': r})
 
def getResponse(board):
    response=''

    for foo in board:
        for oof in foo:
            response+=oof
    return response



def getMove(board):


    moves = possibleMoves(board)

    #randMove(board)
    winner = won(board)

    


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
                print('winner ',team,' horizontal on: ',c-1)
                winner=team

    #vertical
    teams = ['x','o']
    for team in teams:
        for foo in range(0,3):
            count =0
            for oof in range(0,3):
                if board[oof][foo] == team:
                        count+=1
            if count == 3:
                    print('winner ',team,' vertical on: ',foo)
                    winner=team
    #diagonal
    teams = ['x','o']
    for team in teams:
        if board[0][0]==team and board[1][1]==team and board[2][2]==team:
            print('winner ',team,' diagonal on: 0')
            winner=team
        if board[2][0]==team and board[1][1]==team and board[0][2]==team:
            print('winner ',team,' diagonal on: 1')
            winner=team

    return winner




def possibleMoves(board):
    moves = []
    for foo in range(0,3):
        for oof in range(0,3):
            if(board[foo][oof]=='_'):
                moves.append([foo,oof])

    return moves




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
















