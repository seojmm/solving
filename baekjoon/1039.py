import sys
import collections
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N, K = map(int, input().split())

q = collections.deque()
visited = set()
q.append((N, 0))
ans = 0
while q:
    n, k = q.popleft()
    if k == K:
        ans = max(ans, n)
        continue
    n = list(str(n))
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if i == 0 and n[j] == '0':
                continue
            n[i] , n[j] = n[j], n[i]
            nn = int("".join(n))
            if (nn, k+1) not in visited:
                q.append((nn, k+1))
                visited.add((nn, k+1))
            n[i] , n[j] = n[j], n[i]
    
if ans == 0: print(-1)
else: print(ans)

