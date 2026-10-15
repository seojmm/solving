import sys
input = sys.stdin.readline

K = int(input())

dp = [(0, 1)]

for i in range(1, K):
    tmp = (dp[i-1][1], dp[i-1][1]+dp[i-1][0])
    dp.append(tmp)

# print(dp)
print(f'{dp[-1][0]} {dp[-1][1]}')
