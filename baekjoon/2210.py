import sys
import collections

sys.setrecursionlimit = 10**6
input = sys.stdin.readline

S = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(input().split()) for _ in range(5)]


def dfs(x, y, ss):
    if len(ss) == 6:
        S.add(ss)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, ss + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(S))
