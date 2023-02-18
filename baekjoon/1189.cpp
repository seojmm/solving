#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int R, C, K;
int ans = 0;
char board[6][6];
bool visited[6][6] = {false, };
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

void dfs(int x, int y, int dist){
    if(x == 1 && y == C && dist == K){
        ans++;
        return;
    }
    else if(dist > K) return;
    
    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx < 1 || nx > R || ny < 1 || ny > C) continue;
        if(visited[nx][ny]) continue;
        if(board[nx][ny] == 'T') continue;
        visited[nx][ny] = true;
        dfs(nx, ny, dist+1);
        visited[nx][ny] = false;
    }
    
}

int main(){
    scanf("%d %d %d", &R, &C, &K);
    string li;
    for(int i=1; i<=R; i++){
        cin >> li;
        for(int j=1; j<=C; j++){
            board[i][j] = li.at(j-1);
        }
        
    }
    visited[R][1] = true;
    dfs(R, 1, 1);
    printf("%d\n", ans);
    
    return 0;
}
