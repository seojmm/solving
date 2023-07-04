#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int T;
string pattern;


int main(){
    scanf("%d", &T);
    while(T--){
        cin >> pattern;
        
        int idx = 0;
        bool ans = true;
        while(ans && idx < pattern.length()){
            if(pattern[idx] == '1'){ // (100+1+)+
                idx++;
                // 다음 1까지 2칸 미만으로 띄워져 있는 경우
                int next1 = pattern.find('1', idx);
                if(next1 == string::npos || next1 - idx < 2){
                    ans = false;
                    continue;
                }
                
                int next0 = pattern.find('0', next1);
                if(next0 == pattern.length()-1){
                    ans = false;
                    continue;
                }
                if(next0 == string::npos){
                    idx = pattern.length();
                    continue;
                }
                
                idx = next0;
                if(pattern[next0 + 1] == '0' && next0 - next1 > 1){
                    idx--;
                    continue;
                }
                
            }
            else{ // (01)+
                if(pattern[++idx] != '1' || pattern.length() <= idx) ans = false;
                idx++;
                continue;
            }
        }
        
        (idx == pattern.length() && ans) ? printf("YES\n") : printf("NO\n");
        
    }
    
    return 0;
}
