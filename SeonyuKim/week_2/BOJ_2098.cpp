#include <bits/stdc++.h>

using namespace std;

const int INF = 1000000000; // 매우 큰 값으로, 경로가 없을 때 사용
int N;                     // 도시의 개수
int cost[17][17];          // 각 도시 간 이동 비용. (N ≤ 16 가정)
int dp[1 << 16][16];       // dp[mask][cur]: 방문 상태가 mask이고, 현재 도시가 cur일 때의 최소 총 비용.
// dp의 mask는 비트마스크로, 각 비트는 해당 도시가 방문되었는지 나타냅니다.

/// 재귀 함수 tsp(mask, cur):
/// mask: 현재까지 방문한 도시들의 집합 (비트마스크)
/// cur: 현재 위치한 도시
/// 반환값: 현재 상태에서 시작 도시(0번)로 돌아가기까지의 최소 총 비용 (경로가 없는 경우 INF)
int tsp(int mask, int cur) {
    // 모든 도시 방문 완료한 경우(모든 비트가 1이면)
    if (mask == (1 << N) - 1) {
        // 마지막 도시에서 시작 도시(0)로 돌아갈 수 있다면 그 경로의 비용, 아니라면 INF
        return cost[cur][0] ? cost[cur][0] : INF;
    }
    
    int &res = dp[mask][cur];
    if (res != -1) return res; // 메모이제이션된 결과가 있으면 바로 반환
    
    res = INF;
    // 다음 방문할 도시를 탐색
    for (int next = 0; next < N; next++) {
        // next 도시가 아직 방문되지 않았고, cur에서 next로 이동할 수 있는 경우
        if (!(mask & (1 << next)) && cost[cur][next] != 0) {
            res = min(res, cost[cur][next] + tsp(mask | (1 << next), next));
        }
    }
    
    return res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    // 도시의 개수를 입력받고, cost 배열을 채웁니다.
    cin >> N;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> cost[i][j];
        }
    }
    
    // dp 배열을 -1로 초기화 (아직 계산되지 않은 상태를 의미)
    for (int mask = 0; mask < (1 << N); mask++){
        for (int i = 0; i < N; i++){
            dp[mask][i] = -1;
        }
    }
    
    // 시작 도시를 0으로 정하고, 방문 상태 마스크는 1 (즉, 도시 0만 방문한 상태)로 시작
    int answer = tsp(1, 0);
    cout << answer << "\n";
    return 0;
}