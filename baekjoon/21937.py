import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

cnt = 0
N, M = map(int, input().rstrip().split())
graph = collections.defaultdict(list)
visited = [False]*(N+1)
for _ in range(M):
    x, y = map(int, input().rstrip().split())
    graph[y].append(x)
X = int(input().rstrip())

def dfs(start):
    global cnt
    
    for vertex in graph[start]:
        if not visited[vertex]:
            cnt += 1
            visited[vertex] = True
            dfs(vertex)

dfs(X)
print(cnt)