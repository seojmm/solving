#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int N, M;
int map[101][101];
int visited[101][101];
int outAir[101][101];
int cnt = 0;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

void outer(){
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));

    while(!q.empty()){
        pair<int, int> p = q.front();
        q.pop();

        if(visited[p.first][p.second]) continue;
        visited[p.first][p.second] = 1;
        
        for(int i=0; i<4; i++){
            int nx = p.first + dx[i];
            int ny = p.second + dy[i];
            if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            
            if(map[nx][ny] == 1){
                outAir[nx][ny]++;
            }
            else if(visited[nx][ny] == 0){
                q.push(make_pair(nx, ny));
            }
        }

    }
}

bool melt(){
    bool isMelted = false;

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(outAir[i][j] >= 2){
                map[i][j] = 0;
                isMelted = true;
            }
        }
    }

    return isMelted;
}

int main(){
    scanf("%d %d", &N, &M);
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            scanf("%d", &map[i][j]);
        }
    }

    while(true){
        memset(visited, 0, sizeof(visited));
        memset(outAir, 0, sizeof(outAir));
        outer();
        bool isMelted = melt();
        if(!isMelted) break;
        cnt++;
    }

    printf("%d", cnt);
    

    return 0;
}