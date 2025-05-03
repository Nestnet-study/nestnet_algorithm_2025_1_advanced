#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> board(n, vector<int>(m));
    int total_cheese = 0; // 전체 치즈 개수를 세서 종료 조건으로 사용
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 1) {
                total_cheese++;
            }
        }
    }

    // 상하좌우 이동을 위한 배열
    int dy[] = {-1, 1, 0, 0};
    int dx[] = {0, 0, -1, 1};

    int time = 0; // 경과 시간

    // 모든 치즈가 녹을 때까지 반복
    while (total_cheese > 0) {
        time++; // 1시간 경과

        // 외부 공기영역을 BFS로 탐색 및 표시 
        vector<vector<bool>> visited(n, vector<bool>(m, false)); // 매 시간마다 방문 배열 초기화
        queue<pair<int, int>> q;
        // BFS 시작점: (0, 0) 좌표 (외부 공기 영역의 시작점)
        if (board[0][0] == 0) {
             q.push({0, 0});
             visited[0][0] = true;
        }

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();
            int y = curr.first;
            int x = curr.second;

            // 현재 칸의 4방향 이웃 탐색
            for (int i = 0; i < 4; ++i) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                // 이웃이 격자 범위 벗어나면 스킵
                if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                // 이미 방문한 곳이면 스킵
                if (visited[ny][nx]) continue;
                // 이웃이 치즈 칸이면 외부 공기 탐색 경로가 아님 -> 스킵
                if (board[ny][nx] == 1) continue;

                // 이웃이 빈 공간(0)이고 아직 방문 안 했으면 큐에 넣고 방문 표시
                visited[ny][nx] = true;
                q.push({ny, nx});
            }
        }
        // BFS 종료 후, visited[y][x] == true인 모든 (y,x)는 현재 시간 기준의 '외부 공기' 영역
        vector<pair<int, int>> melting_cells; // 이번 시간에 녹을 치즈 목록
        for (int y = 0; y < n; ++y) {
            for (int x = 0; x < m; ++x) {
                if (board[y][x] == 1) { // 현재 칸이 치즈인 경우
                    int outside_air_contacts = 0; // 외부 공기 접촉면 수

                    // 치즈 칸의 4방향 이웃 확인
                    for (int i = 0; i < 4; ++i) {
                        int ny = y + dy[i];
                        int nx = x + dx[i];
                        if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                        // 이웃 칸이 '빈 공간(0)'이고, 1번 단계의 BFS에서 '외부 공기'로 확인된 곳(visited[ny][nx] == true)이라면
                        if (board[ny][nx] == 0 && visited[ny][nx]) {
                            outside_air_contacts++; // 외부 공기 접촉면 수 증가
                        }
                    }
                    // 외부 공기 접촉면이 2개 이상이면 녹을 치즈 목록에 추가
                    if (outside_air_contacts >= 2) {
                        melting_cells.push_back({y, x});
                    }
                }
            }
        }

        // 만약 이번 시간에 녹을 치즈가 없다면 (melting_cells가 비어있다면)  종료
        if (melting_cells.empty()) {
             time--;
             break; 
        }
        // 녹을 치즈 목록에 있는 칸들을 실제로 빈 공간(0)으로 변경
        for (const auto& cell : melting_cells) {
            board[cell.first][cell.second] = 0;
        }
        // 전체 치즈 개수 업데이트
        total_cheese -= melting_cells.size();
    } // while(total_cheese > 0) 루프 끝

    cout << time << endl;

    return 0;
}