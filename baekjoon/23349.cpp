#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>

using namespace std;

int N;
string a, b, c, d;
map<string, string> np;
map<string, int*> t;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        cin >> a >> b >> c >> d;
        if(np.find(a) == np.end()){
            np[a] = b;
            if(t[b] == nullptr){
                t[b] = new int[50001];
            }
            int tmpp = stoi(c);
            int tmp = stoi(d);
            for(int j=tmpp; j<tmp; j++){
                t[b][j]++;
            }
        }
        
        
        
    }
    
    
    
    return 0;
}
