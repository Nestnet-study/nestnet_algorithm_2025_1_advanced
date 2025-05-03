#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int m, n, h;
int box[100][100][100];

queue<vector<int>> q;

int main() {
	cin >> m >> n >> h;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				cin >> box[i][j][k];
				
				if (box[i][j][k] == 1)
					q.push({ i, j, k });
			}
		}
	}

	vector<int> cur;
	int dx[] = { -1, 1, 0, 0, 0, 0 };
	int dy[] = { 0, 0, -1, 1, 0, 0 };
	int dz[] = { 0, 0, 0, 0, -1, 1 };

	while (!q.empty()) {
		cur = q.front(); q.pop();
		for (int dir = 0; dir < 6; dir++) {
			int nx = cur[0] + dx[dir];
			int ny = cur[1] + dy[dir];
			int nz = cur[2] + dz[dir];
			
			if (nx < 0 || nx >= h || ny < 0 || ny >= n || nz < 0 || nz >= m)
				continue;
			if (box[nx][ny][nz] != 0)
				continue;

			q.push({ nx, ny, nz });
			box[nx][ny][nz] = box[cur[0]][cur[1]][cur[2]] + 1;
		}
	}

	int max_value = 1;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				if (box[i][j][k] == 0) {
					cout << -1 << endl;
					return 0;
				}
				if (box[i][j][k] > max_value)
					max_value = box[i][j][k];
			}
		}
	}

	cout << max_value - 1 << endl;
}