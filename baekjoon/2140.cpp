#include <iostream>
#include <vector>

using namespace std;

int N, ans = 0;
vector<string> board;
int check[101][101];
int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

int main(){
    scanf("%d", &N);
    
    string tmp;
    for(int i=0; i<N; i++){
        cin >> tmp;
        board.push_back(tmp);
    }
    
    for(int i=1; i<N-1; i++){
        for(int j=1; j<N-1; j++){
            bool flag = true;
            for(int k=0; k<8; k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                
                if(board[nx][ny] == '0'){
                    board[i][j] = '*';
                    flag = false;
                    break;
                }
            }
            if(flag){
                for(int k=0; k<8; k++){
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    
                    if(board[nx][ny] > '0'){
                        board[nx][ny]--;
                    }
                }
            }
        }
    }
    
    for(int i=1; i<N-1; i++){
        for(int j=1; j<N-1; j++){
            if(board[i][j] == '#'){
                ans++;
            }
        }
    }
    
    printf("%d\n", ans);
    
    return 0;
}
