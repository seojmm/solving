import sys
import collections
input = sys.stdin.readline

N = int(input())
dp = [0]*31
dp[1] = 0
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = 3*dp[i-2]
    for j in range(4, i, 2):
        dp[i] += 2*dp[i-j]
    dp[i] += 2
print(dp[N])