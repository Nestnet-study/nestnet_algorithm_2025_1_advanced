/*
인접한 칸끼리 연결된 1을 모양이라고 한다.
모양의 크기는 모양에 포함된 1의 개수이다.

배열의 칸 하나를 바꿔서 만들 수 있는 모양의 최대 크기를 구해라.

대부분의 경우에는 0을 1로 바꿔야겠네.
최대 크기의 모양을 만들어야 하니까 1을 0으로 바꾸면 무조건 크기에 1 이상의 손해를 주게 되겠지.

더 큰 모양을 만들어야 하니까 가능하면 이미 존재하는 모양에 인접한 0을 1로 바꿔야 한다.

0과 1의 개수는 하나 이상임이 조건을 통해 보장되므로 예외는 없다.


n, m: 배열의 크기 (2 <= n, m <= 1000).
arr: 배열. (n, m)의 크기를 가진다.

possible: 배열. arr에서 값을 바꿀 만한 좌표를 저장한다.

1. n, m 입력
2. arr 입력
3. arr 탐색 (n * m)
	a. 값이 1인 원소에 대해 인접한 0의 좌표를 possible에 저장

탐색을 할 때 count 값을 선언해둔다. 기본값은 1.
visited 배열은 탐색 도중 방문한 원소를 저장한다. 기본값은 0.
탐색한 원소들의 값을 visited 배열에서 count로 설정한다.
원소들의 개수를 세서 배열 area에 저장한다. 인덱스는 count.
한 번 탐색을 마칠 때마다 count 값을 1 늘린다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int arr[1000][1000];
int visited[1000][1000] = { 0, };
int area[100001] = { 0, };

vector<pair<int, int>> possible;

bool is_added(vector<int>, int);

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> arr[i][j];
	
	queue<pair<int, int>> q;
	pair<int, int> cur;
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };
	int shape_count = 1;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (visited[i][j])
				continue;
			if (arr[i][j] < 1)
				continue;

			int area_size = 1;

			q.push({ i, j });
			visited[i][j] = shape_count;
			while (!q.empty()) {
				cur = q.front(); q.pop();
				for (int dir = 0; dir < 4; dir++) {
					int nx = cur.first + dx[dir];
					int ny = cur.second + dy[dir];

					if (nx < 0 || nx >= n || ny < 0 || ny >= m)
						continue;
					if (visited[nx][ny])
						continue;
					if (arr[nx][ny] < 1) {
						if (arr[nx][ny] == 0) {
							possible.push_back({ nx, ny });
							arr[nx][ny] = -1;
						}
						continue;
					}
					q.push({ nx, ny });
					visited[nx][ny] = shape_count;

					area_size++;
				}
			}
			area[shape_count] = area_size;

			shape_count++;
		}
	}
	
	int ans = 0;

	for (int i = 0; i < possible.size(); i++) {
		vector<int> already_added;
		int value = 1;

		cur = possible[i];
		for (int dir = 0; dir < 4; dir++) {
			int nx = cur.first + dx[dir];
			int ny = cur.second + dy[dir];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (visited[nx][ny] < 1)
				continue;
			if (is_added(already_added, visited[nx][ny]))
				continue;

			value += area[visited[nx][ny]];
			already_added.push_back(visited[nx][ny]);
		}
		
		if (value > ans)
			ans = value;
	}

	cout << ans << endl;
}

bool is_added(vector<int> list, int value) {
	for (int i = 0; i < list.size(); i++) {
		if (list[i] == value)
			return true;
	}
	return false;
}