import sys
import collections
sys.setrecursionlimit(10**5)

def dfs(cur, prev):
    global ans
    maxFromLeaf = 0
    for next in graph[cur]:
        if next != prev:
            maxFromLeaf = max(maxFromLeaf, dfs(next, cur))
    if maxFromLeaf >= D:
        ans += 1

    return maxFromLeaf + 1

N, S, D = map(int, input().rstrip().split())
graph = collections.defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

dfs(S, 0)
print(2*(ans-1) if ans else 0)
            
