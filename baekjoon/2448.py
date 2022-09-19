import sys
import collections
input = sys.stdin.readline

N = int(input())
board = [[" "]*2*N for _ in range(N)]

def stars(size, x, y):
    if size == 3:
        board[x][y] = "*"
        board[x+1][y-1] = board[x+1][y+1] = "*"
        for i in range(-2, 3):
            board[x+2][y+i] = "*"
    
    else:
        nextSize = size//2
        stars(nextSize, x, y)
        stars(nextSize, x + nextSize, y - nextSize)
        stars(nextSize, x + nextSize, y + nextSize)

stars(N, 0, N-1)
for star in board:
    print("".join(star))