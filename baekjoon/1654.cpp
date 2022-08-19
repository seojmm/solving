#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

unsigned int K, N, ans = 0;
unsigned int arr[10001] = {0, };

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> K >> N;
    for(int i=1; i<=K; i++){
        cin >> arr[i];
    }
    sort(arr+1, arr+K+1);

    if(N==1) ans = arr[K];
    else{
        unsigned int l = 1;
        unsigned int r = arr[K];
        unsigned int mid = (l+r)/2;
        unsigned int tmp = 0;

        while(l <= r){
            mid = (l + r)/2;
            tmp = 0;
            for(int i=1; i<=K; i++){
                tmp += arr[i]/mid;
            }
            
            if(tmp < N) r = mid-1;
            else if(tmp >= N){
                l = mid + 1;
                ans = max(ans, mid);
            }
        }
    }

    cout << ans << '\n';

    return 0;
}