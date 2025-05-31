#include <bits/stdc++.h> 
using namespace std;     

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);                    

    int N, M; 
    cin >> N >> M;

   
    map<int, int> warp; 
    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        warp[x] = y; 
    }
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        warp[u] = v; 
    }

    
    vector<int> dist(101, -1); 
    queue<pair<int, int>> q; 


    q.push({1, 0});
    dist[1] = 0;

    while (!q.empty()) {
        int current_pos = q.front().first;
        int current_rolls = q.front().second;
        q.pop();

        // 목표 지점 도달
        if (current_pos == 100) {
            cout << current_rolls << '\n'; 
            return 0; 
        }

        // 주사위 굴리기 (1부터 6까지)
        for (int dice = 1; dice <= 6; ++dice) {
            int next_pos_candidate = current_pos + dice;

            if (next_pos_candidate > 100) { 
                continue;
            }

            // 사다리 또는 뱀이 있는지 확인 (map 변수 사용)
            int final_next_pos = next_pos_candidate;
            if (warp.count(next_pos_candidate)) { // 해당 위치에 워프 정보가 있다면
                final_next_pos = warp[next_pos_candidate]; // map에서 도착 위치를 가져옴
            }

            // 아직 방문하지 않은 칸이라면 (최단 경로 보장)
            if (dist[final_next_pos] == -1) {
                dist[final_next_pos] = current_rolls + 1; // 주사위 굴린 횟수 1 증가
                q.push({final_next_pos, current_rolls + 1}); // 큐에 다음 상태 추가
            }
        }
    }

    return 0; // 일반적으로 100번 칸에 도달하므로 이 라인은 실행되지 않음
}