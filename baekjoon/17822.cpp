#include <iostream>
#include <vector>
#include <set>
using namespace std;

int N, M, T, x, d, k, sum = 0;
vector<int> v[51];
set<pair<int, int>> s;

// n번째 원반을 한 칸 회전하는 함수
void rotate(int n, int d)
{
    if (!d)
    {
        int last = v[n][M];
        for (int i = M; i > 1; i--)
        {
            v[n][i] = v[n][i - 1];
        }
        v[n][1] = last;
    }
    else
    {
        int first = v[n][1];
        for (int i = 1; i <= M - 1; i++)
        {
            v[n][i] = v[n][i + 1];
        }
        v[n][M] = first;
    }
}

// 같으면 0, 다르면 그대로
void convert(int i1, int j1, int i2, int j2)
{
    if (v[i1][j1] && v[i1][j1] == v[i2][j2])
    {
        // v[i1][j1] = 0;
        // v[i2][j2] = 0;
        s.insert({i1, j1});
        s.insert({i2, j2});
    }
}

int main()
{
    scanf("%d %d %d", &N, &M, &T);

    int tmp;
    for (int i = 1; i <= N; i++)
    {
        v[i].push_back(-1);
        for (int j = 1; j <= M; j++)
        {
            scanf("%d", &tmp);
            sum += tmp;
            v[i].push_back(tmp);
        }
    }

    while (T--)
    {
        scanf("%d %d %d", &x, &d, &k);
        // x의 배수인 원판을 d방향으로 k칸 회전.

        for (int i = x; i <= N; i += x)
        {
            for (int j = 1; j <= k; j++)
            {
                rotate(i, d);
            }
        }

        // for (int i = 1; i <= N; i++)
        // {
        //     for (int j = 1; j <= M; j++)
        //     {
        //         printf("%d ", v[i][j]);
        //     }
        //     printf("\n");
        // }

        //인접한 수 없애기
        for (int i = 1; i <= N; i++)
        {
            // convert(i, 1, i, 2);
            convert(i, 1, i, M);
            // convert(i, M, i, M - 1);
            for (int j = 1; j <= M - 1; j++)
            {
                // convert3(i, j - 1, i, j, i, j + 1);
                convert(i, j, i, j + 1);
            }
        }
        for (int j = 1; j <= M; j++)
        {
            // convert(1, j, 2, j);
            // convert(N, j, N - 1, j);
            for (int i = 1; i <= N - 1; i++)
            {
                // convert3(i - 1, j, i, j, i + 1, j);
                convert(i, j, i + 1, j);
            }
        }
        // for (pair<int, int> e : s)
        // {
        //     printf("!!%d %d\n", e.first, e.second);
        // }

        // 지울 것이 없는 경우
        if (s.empty())
        {
            int nums = 0;
            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= M; j++)
                {
                    if (v[i][j] > 0)
                        nums++;
                }
            }
            double avg = double(sum) / nums;
            // printf("%d %d\n", sum, nums);
            // for (int i = 1; i <= N; i++)
            // {
            //     for (int j = 1; j <= M; j++)
            //     {
            //         printf("%d ", v[i][j]);
            //     }
            //     printf("\n");
            // }
            // printf("%lf\n", avg);
            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= M; j++)
                {
                    if (v[i][j] && v[i][j] < avg)
                    {

                        v[i][j] += 1;
                        sum += 1;
                    }
                    else if (v[i][j] && v[i][j] > avg)
                    {

                        v[i][j] -= 1;
                        sum -= 1;
                    }
                }
            }
        }
        else
        {
            // for (int i = 1; i <= N; i++)
            // {
            //     for (int j = 1; j <= M; j++)
            //     {
            //         printf("%d ", v[i][j]);
            //     }
            //     printf("\n");
            // }

            // 지울 것이 있는 경우
            for (pair<int, int> elem : s)
            {
                // printf("%d %d\n", elem.first, elem.second);
                sum -= v[elem.first][elem.second];
                v[elem.first][elem.second] = 0;
            }
            // for (int i = 1; i <= N; i++)
            // {
            //     for (int j = 1; j <= M; j++)
            //     {
            //         printf("%d ", v[i][j]);
            //     }
            //     printf("\n");
            // }
        }

        // for (int i = 1; i <= N; i++)
        // {
        //     for (int j = 1; j <= M; j++)
        //     {
        //         printf("%d ", v[i][j]);
        //     }
        //     printf("\n");
        // }
        s.clear();
    }

    printf("%d\n", sum);

    return 0;
}

int imp_lower(int arr[], int target, int N)
{
    int l = 0;
    int r = N;
    while (l < r)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] < target)
            l = mid + 1;
        else
            r = mid;
    }

    return l;
}