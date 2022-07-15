#include <iostream>

using namespace std;

int N, K;
long long dp[201][201] = {
    0,
};

int main()
{
    scanf("%d %d", &N, &K);

    for (int i = 0; i <= 200; i++)
    {
        dp[i][1] = 1;
        dp[i][2] = i + 1;
    }

    for (int i = 0; i <= N; i++)
    {
        for (int j = 3; j <= K; j++)
        {
            for (int k = 0; k <= i; k++)
            {
                dp[i][j] += dp[i - k][j - 1];
            }
            dp[i][j] %= 1000000000;
        }
    }

    printf("%lld\n", dp[N][K]);

    return 0;
}