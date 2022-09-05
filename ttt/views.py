
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
    printBoard(board)
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

    print('getting move')


    randMove(board)

    return board


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
















