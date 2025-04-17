#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> grid[i][j];
        }
    }
    int compId = 2;             // 1의 영역을 구분하기 위한 ID (2부터 시작)
    vector<int> comp(n * m, 0); // 각 영역 넓이 저장
               // 상 하 좌 우
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    // BFS로 1을 탐색하면서 영역 넓이 계산
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (grid[i][j] == 1)
            {
                queue<pair<int, int>> q;
                q.push({i, j});
                grid[i][j] = compId; // 방문 처리
                int area = 1;        // 현재 영역의 넓이를 1(시작 셀)로 초기화

                while (!q.empty()){
                    auto [x, y] = q.front(); // 좌표 (x, y) 가져오기
                    q.pop();                 // 가져온 좌표를 큐에서 제거

                    for (int d = 0; d < 4; d++)
                    {
                        int nx = x + dx[d]; // 상하좌우 탐색
                        int ny = y + dy[d];
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 체크
                        if (grid[nx][ny] == 1)
                        {                          // 방문하지 않은 1을 발견하면
                            grid[nx][ny] = compId; // 방문 처리
                            q.push({nx, ny});      // 큐에 추가
                            area++;                // 영역 넓이 증가
                        }
                    }
                }
                comp[compId] = area; // 현재 영역의 넓이를 저장
                compId++;            // 다음 영역 ID로 증가
            }
        }
    }

    int result = 0; // 최종 결과 저장
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (grid[i][j] == 0){ // 0인 경우에만 탐색
                set<int> visited; // 방문한 영역 ID 저장
                int area = 1;     // 시작 셀 넓이 1로 초기화
                for (int d = 0; d < 4; d++){
                    int nx = i + dx[d]; // 상하좌우 탐색
                    int ny = j + dy[d]; 
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 체크
                    if (grid[nx][ny] > 1){ // 방문한 영역이면
                        visited.insert(grid[nx][ny]); // ID 저장
                    }
                }
                for (auto id : visited){
                    area += comp[id]; // 각 영역의 넓이 더하기
                }
                result = max(result, area); // 최댓값 갱신
            }
        }
    }
    cout << result << "\n";
    return 0;
}
