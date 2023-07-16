import sys
import collections

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
dist_with_gram = 987654321


def bfs(x, y, visited):
    global dist_with_gram
    q = collections.deque()
    q.append((0, 0, 0))
    visited[0][0] = True

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == 2:
                    dist_with_gram = (N-1)-nx + (M-1)-ny + d + 1
                    q.append((nx, ny, d+1))
                    visited[nx][ny] = True
                elif board[nx][ny] == 0:
                    q.append((nx, ny, d+1))
                    visited[nx][ny] = True
                if nx == N-1 and ny == M-1:
                    return min(d+1, dist_with_gram)

    return dist_with_gram


N, M, T = map(int, input().split())

visited = [[False]*M for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, input().split())))


result = bfs(0, 0, visited)

if result > T:
    print("Fail")
else:
    print(result)
