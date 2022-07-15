import sys
import collections
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
LIS = []
dp = [1]*(N+1)

for i in range(1, N+1):
    for j in range(1, i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
# 여기까지는 그냥 LIS 길이 구하는 과정.

LISLen = max(dp)
print(LISLen)

for i in range(N, 0, -1):
    if dp[i] == LISLen:
        LIS.append(A[i])
        LISLen -= 1

print(*LIS[::-1])
