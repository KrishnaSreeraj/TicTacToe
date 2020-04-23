# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:35:58 2020

@author: acer
"""


import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s = 'X'
p2s = 'O'

print(numpy.matrix(board))

def entry(symbol):
    while(1):
        row=int(input("Enter the row : "))
        col=int(input("Enter the column : "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            board[row-1][col-1]=symbol
            break
        else:
            print("Invalid entry !! Re-enter row and column !!")
            
def check_row(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if(board[r][c]==symbol):
                count = count+1
        if count==3:
            print(symbol,'won')
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if(board[r][c]==symbol):
                count = count+1
        if count==3:
            print(symbol,'won')
            return True
    return False

            
def diagonal(symbol):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(symbol,'won')
        return True
    if(board[0][1]==board[1][1] and board[1][1]==board[0][2] and board[1][1]==symbol):
        print(symbol,'won')
        return True
    return False
    
def won(symbol):
    return check_row(symbol) or check_col(symbol) or diagonal(symbol)

def play():
    for turn in range(9):
        if(turn%2==0):
            print("X turn : ")
            entry(p1s)
            print(numpy.matrix(board))
            if(won(p1s)):
                break
        else:
            print("O Turn : ")
            entry(p2s)
            print(numpy.matrix(board))
            if(won(p2s)):
                break
    if(not(won(p1s)) and not(won(p2s))):
        print("Draw")
            
play()
    