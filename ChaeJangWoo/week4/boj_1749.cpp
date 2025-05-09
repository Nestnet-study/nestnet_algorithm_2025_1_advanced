#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int Sums[201][201] = {};
int Max = INT_MIN;

int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);
    
    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; ++i)
    {
        int Sum = 0;
        for (int j = 1; j <= M; ++j)
        {
            int Num;
            cin >> Num;
            Sum += Num;

            Sums[i][j] = Sum;
        }

    }

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= M; ++j)
        {
            for (int w = 0; w <= M - j; ++w)
            {
                int Sum = 0;

                for (int h = 0; h <= N - i; ++h)
                {
                    int TempSum = Sums[i + h][j + w] - Sums[i + h][j - 1];

                    Sum += TempSum;
                    Max = max(Sum, Max);
                }
            }
        }
    }

    cout << Max;
}
