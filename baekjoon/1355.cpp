#include <iostream>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;

int LC, LH, H, V;
vector<int> hor;
vector<int> ver;
int cake[201][201] = {
    0,
};

int main()
{
    scanf("%d %d", &LC, &LH);
    for (int i = LC - LH + 1; i <= LC + LH; i++)
    {
        for (int j = LC - LH + 1; j <= LC + LH; j++)
        {
            cake[i][j] = -1; // 구멍
        }
    }
    scanf("%d", &H);

    int tmp;
    for (int i = 0; i < H; i++)
    {
        scanf("%d", &tmp);
        hor.push_back(tmp);
    }
    scanf("%d", &V);
    for (int i = 0; i < V; i++)
    {
        scanf("%d", &tmp);
        ver.push_back(tmp);
    }

    

    for (int i = 1; i <= 2 * LC; i++)
    {
        for (int j = 1; j <= 2 * LC; j++)
        {
            printf("%d ", cake[i][j]);
        }
        printf("\n");
    }

    return 0;
}