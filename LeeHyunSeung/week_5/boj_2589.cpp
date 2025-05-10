#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

struct P { int x; int y; };

int main() {
	int n, m;
	char map[50][51];

	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", map[i]);
	
	queue<P> q;
	P cur;

	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };
	int visited[50][50];
	int ans = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 'W')
				continue;

			memset(visited, -1, sizeof(visited));

			q.push({ i, j });
			visited[i][j] = 0;

			while (!q.empty()) {
				cur = q.front(); q.pop();
				if (visited[cur.x][cur.y] > ans)
					ans = visited[cur.x][cur.y];
				
				for (int dir = 0; dir < 4; dir++) {
					P np = { cur.x + dx[dir], cur.y + dy[dir] };

					if (np.x < 0 || np.x >= n || np.y < 0 || np.y >= m)
						continue;
					if (map[np.x][np.y] == 'W')
						continue;
					if (visited[np.x][np.y] >= 0)
						continue;

					q.push(np);
					visited[np.x][np.y] = visited[cur.x][cur.y] + 1;
				}
			}
		}
	}

	printf("%d\n", ans);
}