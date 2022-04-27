#include <iostream>
#include <algorithm>
#include <vector>
#define INF 987654321
using namespace std;

int n, k;
int coin[101];
int dp[10001];

int main(){
    scanf("%d %d", &n, &k);
    for(int i=1; i<=n; i++){
        scanf("%d", &coin[i]);
    }
    sort(coin+1, coin+n+1);

    for(int i=1; i<=k; i++){
        dp[i] = INF;
    }

    for(int i=1; i<=n; i++){
        for(int j=coin[i]; j<=k; j++){
            dp[j] = min(dp[j], dp[j-coin[i]]+1);
        }
    }

    if(dp[k] == INF){
        printf("-1\n");
    }
    else{
        printf("%d\n", dp[k]);
    }

    return 0;
}