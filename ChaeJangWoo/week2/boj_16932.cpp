#include <iostream>
#include <algorithm>
#include <queue>
#include <map>

#define MAX (1000)

using namespace std;

int N, M;
int graph[MAX][MAX];
int dir[4][2] = { {0,1},{1,0},{0,-1},{-1,0} };
int answer = 0;
int group = 1;
//visited.first = group visited.second = cnt
pair<int, int> visited[MAX][MAX];


//1인 칸들을 그룹화
void BFS(int r, int c) {
	queue<pair<int, int>> q, qq;
	q.push({ r,c });
	qq.push({ r,c });
	int cnt = 1;
	visited[r][c] = { group++,1 };
	while (!q.empty()) {
		int cr = q.front().first;
		int cc = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nr = cr + dir[i][0];
			int nc = cc + dir[i][1];
			if (nr >= 0 && nr < N && nc >= 0 && nc < M && graph[nr][nc] == 1 && visited[nr][nc].second == 0) {
				cnt++;
				visited[nr][nc].second = 1;
				q.push({ nr, nc });
				qq.push({ nr,nc });
			}
		}

	}
	while (!qq.empty()) {
		int cr = qq.front().first;
		int cc = qq.front().second;
		qq.pop();
		visited[cr][cc] = { group, cnt };
	}

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	vector<pair<int, int>> vt;
	//그래프 입력 및 0의 좌표들 저장 (변경할 칸의 좌표)
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> graph[i][j];
			if (graph[i][j] == 0)
				vt.push_back({ i,j });
		}
	}

	//1인 칸들 그룹화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (graph[i][j] == 1 && !visited[i][j].second)
				BFS(i, j);
		}
	}
	//0인 좌표들 탐색
	for (int i = 0; i < vt.size(); i++) {
		int r = vt[i].first;
		int c = vt[i].second;
		int cnt = 1;
		map<int, int> plus;
		for (int j = 0; j < 4; j++) {
			int nr = r + dir[j][0];
			int nc = c + dir[j][1];
			if (nr >= 0 && nr < N && nc >= 0 && nc < M &&graph[nr][nc] == 1) {
				plus[visited[nr][nc].first] = visited[nr][nc].second;
			}
		}
		for (auto o : plus) {
			cnt += o.second;
		}
		answer = max(answer, cnt);
	}

	cout << answer << '\n';
	return 0;
}