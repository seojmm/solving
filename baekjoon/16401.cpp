#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M, N;
vector<int> L;

int main(){
    scanf("%d %d", &M, &N);
    L.resize(N);
    for(int& x: L){
        cin >> x;
    }
    sort(L.begin(), L.end());
    
//    if(M <= N){
//        printf("%d\n", L[M-N]);
//    }

    int lo = 1, hi = L[N-1];
    int mid = 0, result = 0;
    int tmp = 0;
    while(lo <= hi){
        mid = lo+(hi-lo)/2;
        
        tmp = 0;
        for(int i=0; i<N; i++){
            tmp += L[i]/mid;
        }
        if(tmp >= M){
            lo = mid+1;
            result = mid;
        }
        else{
            hi = mid - 1;
        }
        
    }
    
    printf("%d\n", result);
    
    
    return 0;
}
