#include <iostream>
#include <vector>
using namespace std;

int N, x, y, cnt;
int board[101][101];
int dp[101][101];

int main(){
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            scanf("%d", &board[i][j]);
        }
    }

    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(board[i][j] == 0) continue;
            if(dp[i][j]){
                if(i + board[i][j] <= N) dp[i+board[i][j]][j] += dp[i][j];
                if(j + board[i][j] <= N) dp[i][j+board[i][j]] += dp[i][j];
            }
        }
    }
    cout << board[N][N] << endl;


    return 0;
}