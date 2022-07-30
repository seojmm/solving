import sys
import collections
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

graph = collections.defaultdict(list)
N, M = map(int, input().split())

def dfs(n):

    for next in graph[n]:
        if visited[next[0]] != -1:
            continue

        visited[next[0]] += 1 + visited[n] + next[1]
        dfs(next[0])



for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for i in range(M):
    ans = 0
    a, b = map(int, input().split())
    visited = [-1]*(N+1)
    visited[a] = 0
    dfs(a)
    print(visited[b])


