#include <bits/stdc++.h>

using namespace std;


// 6팀의 대결에서 나올 수 있는 경기 페어들을 저장합니다.
vector<pair<int, int>> match = {
    {0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5},
    {1, 2}, {1, 3}, {1, 4}, {1, 5},
    {2, 3}, {2, 4}, {2, 5},
    {3, 4}, {3, 5},
    {4, 5}
};

int win[6], draw[6], lost[6];

bool dfs(int matchIdx) {
    // 모든 경기를 처리했다면 각 팀의 남은 승, 무, 패가 0인지 확인
    if (matchIdx == match.size()) {
        for (int i = 0; i < 6; i++) {
            if (win[i] != 0 || draw[i] != 0 || lost[i] != 0)
                return false;
        }
        return true;
    }
    
    // 현재 경기(두 팀)를 가져옵니다.
    int team1 = match[matchIdx].first;
    int team2 = match[matchIdx].second;
    
    // 경우 1: team1 승, team2 패
    if (win[team1] > 0 && lost[team2] > 0) {
        win[team1]--;
        lost[team2]--;
        if (dfs(matchIdx + 1))
            return true;
        win[team1]++;
        lost[team2]++;
    }
    
    // 경우 2: 두 팀 무승부
    if (draw[team1] > 0 && draw[team2] > 0) {
        draw[team1]--;
        draw[team2]--;
        if (dfs(matchIdx + 1))
            return true;
        draw[team1]++;
        draw[team2]++;
    }
    
    // 경우 3: team1 패, team2 승
    if (lost[team1] > 0 && win[team2] > 0) {
        lost[team1]--;
        win[team2]--;
        if (dfs(matchIdx + 1))
            return true;
        lost[team1]++;
        win[team2]++;
    }
    
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    for (int t = 0; t < 4; t++) {
        bool earlyReject = false;  // 초기 검증에서 걸러졌는지 여부
        int totalWin = 0, totalDraw = 0, totalLost = 0;
        
        // 6개 팀의 결과 읽기 (승, 무, 패)
        for (int i = 0; i < 6; i++) {
            cin >> win[i] >> draw[i] >> lost[i];
            // 각 팀은 반드시 5경기를 치러야 합니다.
            if (win[i] + draw[i] + lost[i] != 5) {
                earlyReject = true;
            }
            totalWin += win[i];
            totalDraw += draw[i];
            totalLost += lost[i];
        }
        
        // 기본 검증: 총 경기 수, 승패의 균형, 무승부가 짝수여야 함
        if (totalWin + totalDraw + totalLost != 30 || totalWin != totalLost || (totalDraw % 2) != 0)
            earlyReject = true;
        
        // 초기 검증이 통과된 경우에 DFS를 시도
        if (!earlyReject && dfs(0))
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }
    
    return 0;
}