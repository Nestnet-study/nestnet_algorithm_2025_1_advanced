#include <bits/stdc++.h>

using namespace std;

const int INF = numeric_limits<int>::max(); // 무한대 값 정의

// 발판 이동 비용 계산 함수 (from != to 인 경우의 '움직임' 비용)
// from: 현재 발판, to: 목표 발판
int get_move_cost(int from, int to) {
    if (from == 0) return 2; // 중앙에서 다른 발판으로 이동 (비용 2)
    if ((from == 1 && to == 2) || (from == 2 && to == 1) ||
        (from == 3 && to == 4) || (from == 4 && to == 3)) {
        return 4;
    }
    // 인접 이동 (그 외 from != to 인 1~4번 사이 이동)
    return 3;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // dp[l][r] : 왼쪽 발이 l, 오른쪽 발이 r 에 있을 때 해당 스텝까지의 최소 에너지
    // DP 테이블 크기 5x5 (발판 0~4)
    vector<vector<int>> dp(5, vector<int>(5, INF));
    dp[0][0] = 0; // 시작 상태: 두 발 모두 중앙(0,0), 비용 0

    int target;
    while (cin >> target && target != 0) {
        // 이번 스텝(target)까지 처리했을 때의 최소 비용을 저장할 새로운 DP 테이블
        // 매 스텝마다 초기화
        vector<vector<int>> dp_new(5, vector<int>(5, INF));

        // 이전 스텝까지의 모든 가능한 상태 (pl, pr) 를 순회
        for (int pl = 0; pl < 5; ++pl) { // 이전 왼쪽 발 위치 (previous left)
            for (int pr = 0; pr < 5; ++pr) { // 이전 오른쪽 발 위치 (previous right)
                if (dp[pl][pr] == INF) continue; // 이전 상태가 도달 불가능했다면, 그 상태에서 전이하는 것은 의미 없음.

                int current_cost = dp[pl][pr]; // 이전 상태까지의 최소 비용        
                // Case 1: 왼쪽 발이 target 을 밟는 경우 
                if (pr != target) {
                    // 왼쪽 발이 pl 에서 target 으로 이동/제자리 하는 비용 계산
                    // 만약 pl == target 이면 왼쪽 발은 이미 target 에 있었으므로 제자리 (비용 1)
                    // 만약 pl != target 이면 왼쪽 발은 pl 에서 target 으로 이동 (비용 get_move_cost(pl, target))
                    int cost1 = (pl == target) ? 1 : get_move_cost(pl, target);
                    // 새로운 상태 (target, pr) 로의 최소 비용 업데이트
                    dp_new[target][pr] = min(dp_new[target][pr], current_cost + cost1);
                }
                // Case 2: 오른쪽 발이 target 을 밟는 경우
                 if (pl != target) {
                    // 오른쪽 발이 pr 에서 target 으로 이동/제자리 하는 비용 계산
                    // 만약 pr == target 이면 오른쪽 발은 이미 target 에 있었으므로 제자리 (비용 1)
                    // 만약 pr != target 이면 오른쪽 발은 pr 에서 target 으로 이동 (비용 get_move_cost(pr, target))
                    int cost2 = (pr == target) ? 1 : get_move_cost(pr, target);
                    // 새로운 상태 (pl, target) 로의 최소 비용 업데이트
                    dp_new[pl][target] = min(dp_new[pl][target], current_cost + cost2);
                 }
            }
        }
        // 한 스텝(target) 처리가 완료되었으므로, dp_new를 현재의 dp로 만듭니다.
        // 다음 스텝에서는 이 dp_new가 이전 상태 테이블이 됩니다.
        dp = dp_new;
    }
    // 모든 스텝(target) 처리 후 최종 최소 에너지 찾기
    int min_total_energy = INF;
    // 최종 dp 테이블에 저장된 모든 가능한 상태들의 최소 비용을 찾습니다.
    for (int l = 0; l < 5; ++l) {
        for (int r = 0; r < 5; ++r) {
             // 도달 가능한 상태 (dp[l][r] != INF) 들 중에서 최솟값 찾기
            min_total_energy = min(min_total_energy, dp[l][r]);
        }
    }
    cout << min_total_energy << endl;

    return 0;
}