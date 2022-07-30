import sys
import collections
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

graph = collections.defaultdict(list)

def dfs(start):

    for next in graph[start]:
        if visited[next] == -1:
            visited[next] += visited[start] + 2
            dfs(next)

n = int(input())
visited = [-1]*(n+1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    r1, r2 = map(int, input().split())
    graph[r1].append(r2)
    graph[r2].append(r1)

visited[a] += 1

dfs(a)
if visited[b] == 0:
    print(-1)
else: print(visited[b])