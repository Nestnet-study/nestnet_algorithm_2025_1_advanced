#include <bits/stdc++.h> 

using namespace std; 

#define DIRTY 1   
#define CLEAN 0   
#define OBSTACLE -1 

int dy[]{ -1, 1, 0, 0 }; 
int dx[]{ 0, 0, -1, 1 }; 


int boards[21][21]; 
int visited[21][21]; 
int trashToTrashLength[11][11]; 
int startToTrash[11]; 

int w, h; 
char c; 


void bfs(int sy, int sx) {
    queue<pair<int, int>> q;
    q.push({ sy, sx });

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            visited[i][j] = INT_MAX;
        }
    }
    visited[sy][sx] = 0; 

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        int current_dist = visited[y][x]; 

        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d]; 
            int nx = x + dx[d];
            int next_dist = current_dist + 1; 

            if (ny >= 0 && ny < h && nx >= 0 && nx < w && boards[ny][nx] != OBSTACLE && visited[ny][nx] > next_dist) {
                visited[ny][nx] = next_dist; 
                q.push({ ny, nx }); 
            }
        }
    }
}

int findMinPath(int robot_y, int robot_x, vector<pair<int, int>>& dirtyPoints) {
    int num_dirty = dirtyPoints.size(); 

    bfs(robot_y, robot_x);
    for (int i = 0; i < num_dirty; i++) {
        startToTrash[i] = visited[dirtyPoints[i].first][dirtyPoints[i].second];
        if (startToTrash[i] == INT_MAX) {
            return -1;
        }
    }

    for (int i = 0; i < num_dirty; i++) {
        bfs(dirtyPoints[i].first, dirtyPoints[i].second);
        for (int j = 0; j < num_dirty; j++) {
            if (i == j) continue; 
            trashToTrashLength[i][j] = visited[dirtyPoints[j].first][dirtyPoints[j].second];
            if (trashToTrashLength[i][j] == INT_MAX) {
                 return -1;
            }
        }
    }
    vector<int> p(num_dirty); 
    for (int i = 0; i < num_dirty; ++i) {
        p[i] = i; 
    }

    int min_total_dist = INT_MAX; 

    do {
        int current_sum = startToTrash[p[0]]; 
        bool possible_permutation = true;

        for (int i = 0; i < num_dirty - 1; ++i) {
            if (trashToTrashLength[p[i]][p[i+1]] == INT_MAX) {
                possible_permutation = false;
                break;
            }
            current_sum += trashToTrashLength[p[i]][p[i+1]];
        }

        if (possible_permutation) {
            min_total_dist = min(min_total_dist, current_sum); 
        }

    } while (next_permutation(p.begin(), p.end())); 


    if (min_total_dist == INT_MAX) {
        return -1;
    }

    return min_total_dist; 
}

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int startY, startX;

    while (cin >> w >> h && (w != 0 || h != 0)) {

        for(int i=0; i<h; ++i) {
            for(int j=0; j<w; ++j) {
                boards[i][j] = CLEAN; 
            }
        }
         for(int i=0; i<11; ++i) {
            startToTrash[i] = 0;
            for(int j=0; j<11; ++j) {
                trashToTrashLength[i][j] = 0;
            }
        }

        vector<pair<int, int>> dirtyPoints; 

        for (int i = 0; i < h; i++) { 
            for (int j = 0; j < w; j++) { 
                cin >> c;
                if (c == '*') {
                    boards[i][j] = DIRTY;
                    dirtyPoints.push_back({ i, j }); 
                } else if (c == 'x') {
                    boards[i][j] = OBSTACLE; 
                } else if (c == 'o') {
                    startY = i;
                    startX = j; 
                }
            }
        }
        cout << findMinPath(startY, startX, dirtyPoints) << endl;
    }

    return 0;
}
