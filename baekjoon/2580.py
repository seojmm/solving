import sys
import collections
input = sys.stdin.readline
SIZE_BOARD = 9
board = [list(map(int, input().split())) for _ in range(SIZE_BOARD)]
visited = [[0]*SIZE_BOARD for _ in range(SIZE_BOARD)]

def sudoku(x, y):
    if board[x][y] != 0:
        return
    
    for i in range(1, 10):
        