import sys
import collections
input = sys.stdin.readline

V, E = map(int, input().split())
INF = 987654321

graph = [[0]*(V+1) for _ in range(V+1)]
dist = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    dist[a][b] = c

for i in range(1, V+1):
    graph[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if dist[i][j] != INF and dist[j][i] != INF:
            ans = min(ans, dist[i][j] + dist[j][i])

print(ans if ans < INF else -1)
