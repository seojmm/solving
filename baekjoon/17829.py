import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, size):
    if size == 2:
        ans = [board[x][y], board[x+1][y], board[x][y+1], board[x+1][y+1]]
        ans.sort()
        return ans[-2]

    size //= 2
    a = divide(x, y, size)
    b = divide(x, y + size, size)
    c = divide(x + size, y, size)
    d = divide(x + size, y + size, size)
    ans = [a, b, c, d]
    ans.sort()
    return ans[-2]

print(divide(0, 0, N))
