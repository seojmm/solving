import sys
import collections
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [987654321]*1001
dp[0] = 0

for i in range(N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + P[j])

print(dp[N])
