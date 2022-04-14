import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = collections.defaultdict(list)
visited = [0]*(n+1)
for i in range(1, n+1):
    l = list(map(int, input().rstrip().split()))
    graph[i] = l[1:]

q = collections.deque()
for i in range(1, n+1):
    flag = True
    if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        while q and flag:
            x = q.popleft()
            for next in graph[x]:
                if visited[next] == 0:
                    q.append(next)
                    visited[next] = -visited[x]
                elif visited[next] == visited[x]:
                    flag = False
                    break
        
    if not flag:
        break

counter = collections.Counter(visited[1:])
print(counter[1])
for i in range(1, n+1):
    if visited[i] == 1:
        print(i, end=" ")
print()
print(counter[-1])
for i in range(1, n+1):
    if visited[i] == -1:
        print(i, end=" ")