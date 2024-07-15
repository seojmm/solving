import sys
import collections
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())
# pos_list = []

board = [['.']*(M+1) for _ in range(N+1)]
visited = [[False]*(M+1) for _ in range(N+1)]
ans = 0
q = collections.deque()

for _ in range(K):
    # pos_list.append(tuple(map(int, input().split())))
    x, y = map(int, input().split())
    board[x][y] = '#'

def bfs(x, y):
    q.clear()
    q.append((x, y))
    visited[x][y] = True
    area = 1
    
    while len(q) > 0:
        x, y = q.popleft()

        if board[x][y] == '#':
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 < nx < N+1 and 0 < ny < M+1 and not visited[nx][ny] and board[nx][ny] == '#':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1

    return area
    

for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            area = bfs(i, j)
            ans = max(ans, area)

print(ans)
