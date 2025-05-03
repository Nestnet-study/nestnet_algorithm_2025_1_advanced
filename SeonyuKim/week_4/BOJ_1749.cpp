#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    // n: 행의 개수, m: 열의 개수
    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < m; ++j){
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> prefix_sum(n + 1, vector<int>(m + 1, 0));

    // 누적 합 배열 계산
    for (int i = 1; i <= n; ++i){
        for (int j = 1; j <= m; ++j){
            prefix_sum[i][j] = grid[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1];
        }
    }
    
    int max_sum = numeric_limits<int>::min();

    // 부분 직사각형의 왼쪽 위 모서리 (r1, c1)
    for (int r1 = 0; r1 < n; ++r1){
        for (int c1 = 0; c1 < m; ++c1){
            // 부분 직사각형의 오른쪽 아래 모서리 (r2, c2)
            for (int r2 = r1; r2 < n; ++r2){
                for (int c2 = c1; c2 < m; ++c2){
                    // (r1, c1) 부터 (r2, c2) 까지의 부분 직사각형 합 계산
                    // 누적 합 배열은 1-indexed 이므로 인덱스를 +1 해줌
                    int current_sum = prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1];
                    if (current_sum > max_sum){
                        max_sum = current_sum;
                    }
                }
            }
        }
    }

    cout << max_sum << endl;

    return 0;
}