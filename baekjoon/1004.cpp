#include <iostream>
#include <tuple>

using namespace std;

int T, a, b, c, d, n;
//vector<tuple<int, int, int>> planet;
int x, y, z;
int cnt;

double dist(int a, int b, int c, int d){
    return (b-a)*(b-a) + (d-c)*(d-c);
}

int main(){
    scanf("%d", &T);
    while(T--){
        cnt = 0;
        
        scanf("%d %d %d %d", &a, &b, &c, &d);
        scanf("%d", &n);
        
        int distance, con1, con2;
        for(int i=0; i<n; i++){
            scanf("%d %d %d", &x, &y, &z);
            distance = dist(a, x, b, y);
            con1 = distance < z*z ? 1 : 0;
            distance = dist(c, x, d, y);
            con2 = distance < z*z ? 1 : 0;
            
            if(con1 != con2) cnt++;
        }
        
//        for(int i=0; i<n; i++){
//            d = dist(a, x, b, y);
//            con1 = d > get<2>(planet[i])*get<2>(planet[i]) ? 1 : 0;
//            d = dist(c, x, d, y);
//            con1 = d > get<2>(planet[i])*get<2>(planet[i]) ? 1 : 0;
//        }
        
        printf("%d\n", cnt);
        
    }
    
    
    return 0;
}
