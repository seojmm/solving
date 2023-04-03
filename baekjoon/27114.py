import sys
input = sys.stdin.readline

A, B, C, K = map(int, input().split())
energy = [A, B, C]
v = [1, 3, 2]
dp = [10**6+1]*(K+1)
dp[0] = 0

for i in range(3):
    for j in range(K+1):
        if j-energy[i] >= 0:
            dp[j] = min(dp[j], dp[j-energy[i]]+1)


print(dp[K]) if dp[K] < 10**6+1 else print(-1)