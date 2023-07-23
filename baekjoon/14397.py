import sys
import collections

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 0]
dy_odd = [0, 1, 1, 1, 0, -1]
dy_even = [-1, 0, 1, 0, -1, -1]
lands = []
ans = 0

N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

curX, curY = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == '#':
            lands.append((i, j))

for i, j in lands:
    for k in range(6):
        nx = i + dx[k]
        if i%2 == 0:
            ny = j + dy_even[k]
        else:
            ny = j + dy_odd[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if graph[nx][ny] == '.':
            ans += 1

print(ans)