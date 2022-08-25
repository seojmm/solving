import sys
import collections
input = sys.stdin.readline


def bfs(x, y, cnt):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        curX, curY = q.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

            if graph[nx][ny] == 0:
                border[cnt].append((nx, ny))


N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[False]*N for _ in range(N)]
border = collections.defaultdict(list)
cnt = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1

ans = 2*N
islands = len(border)
for i in range(1, islands+1):
    for j in range(i+1, islands+1):
        for a, b in border[i]:
            for c, d in border[j]:
                ans = min(ans, abs(a-c)+abs(b-d)+1)

print(ans)
