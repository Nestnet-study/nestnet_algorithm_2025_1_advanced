#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int arr[100][100] = { 0, };
int visited[100][100] = { 0, };

int main() {
	int n, m;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &arr[i][j]);
		}
	}

	queue<pair<int, int>> q;
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };

	int ans = 0;
	int cheese_count;
	do {
		// 초기화
		queue<pair<int, int>> del;
		cheese_count = 0;
		memset(visited, 0, sizeof(visited));

		// 탐색 시작점: { 0, 0 }
		// 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는다.
		q.push({ 0, 0 });
		visited[0][0] = -1;

		// BFS
		pair<int, int> cur;
		while (!q.empty()) {
			cur = q.front(); q.pop();

			for (int dir = 0; dir < 4; dir++) {
				int nx = cur.first + dx[dir];
				int ny = cur.second + dy[dir];

				if (nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;
				// 바깥과 맞닿은 치즈
				if (arr[nx][ny] == 1) {
					visited[nx][ny]++;
					cheese_count++;
					// 두 면 이상 맞닿아 있다면 삭제 스택에 추가한다.
					// 중복을 막기 위해 2일 때만 스택에 추가한다.
					if (visited[nx][ny] == 2)
						del.push({ nx, ny });
				}
				if (visited[nx][ny])
					continue;

				q.push({ nx, ny });
				visited[nx][ny] = -1;
			}
		}

		// 치즈 삭제
		while (!del.empty()) {
			cur = del.front(); del.pop();
			arr[cur.first][cur.second] = 0;
		}

		ans++;
	} while (cheese_count);

	// ans에서 1을 빼준다.
	// 치즈를 다 없애고 난 뒤, 치즈가 있는지 한 바퀴 더 돌기 때문이다.
	printf("%d\n", ans - 1);
}