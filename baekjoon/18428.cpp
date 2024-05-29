#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>

using namespace std;

int N;
string ans = "YES";
string arr[7][7];
vector<pair<int, int>> v;
int students = 0;
int ob = 3;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

void backtracking(int x, int y){
    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        if(0 < nx && nx <= N && 0 < ny && ny <= N){
            if(arr[nx][ny] == "S"){
                ob--;
                ans = "NO";
                return;
            }
            else if(arr[nx][ny] == "O") continue;
            else if(arr[nx][ny] == "T") continue;
            
            for(int j=1; j<N; j++){
                int nnx = nx + j*dx[j];
                int nny = ny + j*dy[j];
                
                if(0 < nnx && nnx <= N && 0 < nny && nny <= N){
                    if(arr[nnx][nny] == "O") break;
                    else if(arr[nnx][nny] == "T") break;
                    else if(arr[nnx][nny] == "S"){
                        if(ob == 0){
                            ans = "NO";
                            return;
                        }
                        arr[nx][ny] = "O";
                        ob--;
                        break;
                    }
                }
            }
        }
    }
}

int main(){
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cin >> arr[i][j];
            if(arr[i][j] == "T") v.push_back(make_pair(i, j));
            else if(arr[i][j] == "S") students++;
        }
    }
    
    for(int i=0; i<v.size(); i++){
        backtracking(v[i].first, v[i].second);
    }
    
    cout << ans << endl;
    
    
    return 0;
}
