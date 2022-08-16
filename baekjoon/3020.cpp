#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, H, ans_cnt = 0, ans = 987654321;
int ss[100001] = {0, };
int js[100001] = {0, };

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> H;
    for(int i=0; i<N/2; i++){
        cin >> ss[i];
        cin >> js[i];
    }

    sort(ss, ss + N/2);
    sort(js, js + N/2);

    int tmp;
    for(int route=1; route<=H; route++){
        tmp = lower_bound(ss, ss+N/2, route) - ss;
        tmp += upper_bound(js, js+N/2, H - route) - js;
        tmp = N - tmp;

        if(tmp == ans) ans_cnt++;
        else if(tmp < ans){
            ans = tmp;
            ans_cnt = 1;
        } 
    }

    cout << ans << " " << ans_cnt << "\n";
    

    return 0;
}

// lower_bound implementation
int LB(int arr[], int target, int n){
    int l = 0;
    int r = n;
    int mid = l + (r - l)/2; // overflow 방지
    while(l < r){
        mid = l + (r - l)/2;
        if(arr[mid] < target){
            l = mid + 1;
        }
        else{
            r = mid;
        }
    }

    return l;
}

// upper_bound implementation
int UB(int arr[], int target, int n){
    int l = 0;
    int r = n;
    int mid = l + (r - l)/2; // overflow 방지
    while(l < r){
        mid = l + (r - l)/2;
        if(arr[mid] > target){
            r = mid;
        }
        else{
            l = mid + 1;
        }
    }

    return l;
}