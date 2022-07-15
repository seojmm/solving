#include <iostream>
#include <vector>

using namespace std;

int N;
int A[1001];
int dp[1001];
int maxIndex = 1;

int main(){
  int N;
  cin >> N;

  for(int i=1; i<=N; i++){
    cin >> A[i];
  }

  for(int i=1; i<=N; i++){
    dp[i] = 1;

    for(int j=1; j<i; j++){
      if(A[j] < A[i] && dp[i] <= dp[j]){
        dp[i]++;
      }
      if(dp[maxIndex] < dp[i]){
        maxIndex = i;
      }
    }
  }

  cout << dp[maxIndex] << endl;
  


  return 0;
}


