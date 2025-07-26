#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
using namespace std;
const int MIN = -2e5 - 5;

int v[1002][1002];
int dp[1002][1002];
int dp2[1002][1002];

int main() {
    init;

    int N, M;
    cin >> N >> M;

    int h;
    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < M + 1; j++) {
            cin >> h;
            v[i][j] = h;
        }
    }

    fill(&dp[0][0], &dp[N + 1][M + 1], MIN);
    fill(&dp2[0][0], &dp2[N + 1][M + 1], MIN);
    dp[0][1] = 0;
    dp[1][0] = 0;
    dp2[0][1] = 0;
    dp2[1][0] = 0;

    // [1][1]부터 시작하므로, 1행은 무조건 왼쪽부터 채워나가야 함
    for (int j = 1; j < M + 1; j++) {
        dp[1][j] = dp[1][j - 1] + v[1][j];
        dp2[1][j] = dp2[1][j - 1] + v[1][j];
    }

    for (int i = 2; i < N + 1; i++) {
        // 왼쪽부터 채우기
        for (int j = 1; j < M + 1; j++) {
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + v[i][j];
        }
        // 오른쪽
        for (int j = M; j > 0; j--) {
            dp2[i][j] = max(dp2[i - 1][j], dp2[i][j + 1]) + v[i][j];
        }

        for (int j = 1; j < M + 1; j++) {
            dp[i][j] = max(dp[i][j], dp2[i][j]);
            dp2[i][j] = dp[i][j];
        }
    }

    cout << dp[N][M];
}