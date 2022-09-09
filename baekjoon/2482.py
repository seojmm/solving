import sys
import collections
input = sys.stdin.readline

N = int(input())
K = int(input())

if 2*K > N:
    print(0)
else:
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(N+1):
        # dp[N][1] = N, dp[N][2] = N(N-3)//2 <- 대각선의 개수
        dp[i][0] = 1
        dp[i][1] = i

    for i in range(2, N+1):
        for j in range(2, K+1):
            if i == N:
              dp[i][j] = (dp[i-3][j-1] + dp[i-1][j])%1000000003
            else:
              dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%1000000003

    print(dp[N][K])
