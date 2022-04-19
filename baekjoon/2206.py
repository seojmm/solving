import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
cnt = sys.maxsize

N, M = map(int, input().rstrip().split())
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[0]*M for _ in range(N)]
q = collections.deque()
q.append((0, 0, 1, False))
visited[0][0] = True
while q:
    x, y, steps, broke = q.popleft()
    if x == N-1 and y == M-1:
        cnt = min(cnt, steps)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny] == True: continue
        
        if graph[nx][ny] == 0:
            q.append((nx, ny, steps+1, broke))
        elif graph[nx][ny] == 1 and not broke:
            q.append((nx, ny, steps+1, True))
        
        visited[nx][ny] = True

if visited[N-1][M-1] == 0:
    print(-1)
else:
    print(cnt)