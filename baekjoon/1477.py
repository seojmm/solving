import sys
import collections
input = sys.stdin.readline

N, M, L = map(int, input().rstrip().split())

cur = list(map(int, input().rstrip().split()))
cur.append(0)
cur.append(L)
cur.sort()

l, r = 1, L
ans = 0
while l <= r:
    cnt = 0
    mid = l + (r-l)//2
    for i in range(1, N+2):
        if cur[i] - cur[i-1] > mid:
            cnt += (cur[i] - cur[i-1]-1)//mid

    if cnt > M:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid

print(ans)
