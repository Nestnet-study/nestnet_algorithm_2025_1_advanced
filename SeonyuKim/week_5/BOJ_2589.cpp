#include <bits/stdc++.h> 

using namespace std; 


char board[51][51]; 
int visited[51][51];


int dy[] = {-1, 1, 0, 0}; 
int dx[] = {0, 0, -1, 1}; 

int h, w;


int bfs(int sy, int sx) {

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            visited[i][j] = -1; 
        }
    }

    queue<pair<int, int>> q;

    q.push({sy, sx});
    visited[sy][sx] = 0; 

    int max_dist = 0; 

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        max_dist = max(max_dist, visited[y][x]);

        for (int i = 0; i < 4; ++i) {
            int ny = y + dy[i]; 
            int nx = x + dx[i]; 

            if (ny >= 0 && ny < h && nx >= 0 && nx < w && board[ny][nx] == 'L' && visited[ny][nx] == -1) {
                visited[ny][nx] = visited[y][x] + 1; 
                q.push({ny, nx}); 
            }
        }
    }
    return max_dist; 
}

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> h >> w;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> board[i][j];
        }
    }

    int result_dist = 0; 

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (board[i][j] == 'L') {
                int current_bfs_max_dist = bfs(i, j);
                result_dist = max(result_dist, current_bfs_max_dist);
            }
        }
    }

    cout << result_dist << "\n";

    return 0;
}
