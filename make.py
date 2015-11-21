#!/usr/bin python

# MAKES THE BOARD

import sys, os, random

def bprint(board):
    ### PRINT FOR DEBUGGING
    for row in board:
        for col in row:
            sys.stdout.write("%s" % col)
        sys.stdout.write("\n")
    sys.stdout.write("\n")

board_size = 9  #9x9 board
totalmines = board_size
board = [[0 for x in range(board_size)] for x in range(board_size)]  #creates a square of 0s

### PLACE THE MINES
mines = list()
for mine in range(0, totalmines):
    x = random.randrange(0, board_size)
    y = random.randrange(0, board_size)
    mines.append([x,y])
    board[x][y] = 'M'

bprint(board)

### WRITE THE NUMBERS
for r in range(0, board_size):
    for c in range(0, board_size):
        if board[r][c] == 'M':
            continue
        if r > 0 and board[r-1][c]   == 'M':
            board[r][c] += 1
        if r > 0 and c > 0 and board[r-1][c-1] == 'M':
            board[r][c] += 1
        if r > 0 and c < board_size-1 and board[r-1][c+1] == 'M':
            board[r][c] += 1
        if c > 0 and board[r][c-1] == 'M':
            board[r][c] += 1
        if c < board_size-1 and board[r][c+1] == 'M':
            board[r][c] += 1
        if r < board_size-1 and board[r+1][c] == 'M':
            board[r][c] += 1
        if r < board_size-1 and c > 0 and board[r+1][c-1] == 'M':
            board[r][c] += 1
        if r < board_size-1 and c < board_size-1 and board[r+1][c+1] == 'M':
            board[r][c] += 1

#if [r>0 and r-1, c] has mine, +1
#if [r>0 and r-1, c-1] has mine, +1
#if [r>0 and r-1, c+1] has mine, +1
#if [r, c-1] has mine, +1
#if [r, c+1] has mine, +1
#if [r<board_size and r+1, c] has mine, +1
#if [r<bsz and r+1, c-1] has mine, +1
#if [r<bsz and r+1, c+1] has mine, +1

bprint(board)
