#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, b, a;
    cin >> n >> b >> a;

    vector<int> v = vector<int>(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    unsigned long long cost = 0;
    int i;
    for (i = 0; i < n; i++) {
        if (i < a)
            cost += v[i]/2;
        else
            cost += v[i]/2 + v[i - a]/2;
        if (cost > b) break;
    }

    cout << i;

    return 0;
}
