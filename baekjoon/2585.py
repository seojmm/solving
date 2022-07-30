import sys
import collections
import math
import copy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dist2D(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def bfs(v, fuel):
    visited = [0]*(n+1)
    q = collections.deque()
    q.append(v)
    cnt = 0

    while q:
        if cnt > k:
            return False

        while q:
            vertex = q.popleft()
            
            if not visited[vertex]:
                visited[vertex] = 1

                for i in range(1, n+1):
                    dist = dist2D(point[vertex][0], point[vertex][1], point[i][0], point[i][1])
                    if dist <= fuel:
                        dd = dist2D(10000, 10000, point[i][0], point[i][1])
                        if dd <= fuel:
                            return True
                        q.append(i)
        cnt += 1
    
    return False
            

point = []

n, k = map(int, input().split())
if k == 0:
    print(dist2D(0,0, 10000, 10000))
    sys.exit(0)

point = [(0, 0)]
for i in range(n):
    point.append(list(map(int, input().split())))
point.append((10000, 10000))

#print(point)
ans  = 0
lo, hi = 0, dist2D(0, 0, 10000, 10000)
while lo <= hi:
    mid = (lo+hi)//2

    if bfs(0, mid*10):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
        

print(ans)

