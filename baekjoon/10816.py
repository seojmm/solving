import sys
import collections
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
required = list(map(int, input().split()))
ans = [0]*M

card.sort()


for i in range(M):
    l, r = 0, N
    while l<r:
        mid = (r-l)//2 + l
        
        if card[mid] < required[i]:
            l = mid + 1
        else:
            r = mid
            
    j = r
    while j < N and card[j] == required[i]:
        ans[i] += 1
        j += 1

print(*ans)