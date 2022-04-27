import sys
import collections
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    dp[i] = 1
    for j in range(0, i):
        if(A[i] < A[j] and dp[j] + 1 > dp[i]):
            dp[i] = dp[j] + 1

print(max(dp))
