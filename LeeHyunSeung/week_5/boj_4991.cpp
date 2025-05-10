#include <cstdio>
#include <cstring>
#include <climits>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct P { int x; int y; };

int edge[11][11] = { 0, };
int vertex[11] = { 0, };
int vertex_size = 0;

int ans;
int current;
int ind, pos;
void r() {
	if (current > ans)
		return;
	if (ind == vertex_size - 1) {
		if (current < ans)
			ans = current;
		return;
	}

	int temp = pos;
	ind++;
	for (int i = 0; i < vertex_size; i++) {
		if (vertex[i])
			continue;

		current += edge[pos][i];
		vertex[i] = 1;
		pos = i;
		r();
		pos = temp;
		vertex[i] = 0;
		current -= edge[pos][i];
	}
	ind--;
}

int main() {
	while (1) {
		int w, h;
		char room[20][21];
		queue<P> dirty; // 더러운 칸, 로봇 청소기 위치

		vertex_size = 0;
		memset(vertex, 0, sizeof(vertex));
		memset(edge, 0, sizeof(edge));  
		
		scanf("%d %d", &w, &h);

		if (!w && !h)
			break;

		for (int i = 0; i < h; i++) {
			scanf("%s", room[i]);

			for (int j = 0; j < w; j++) {
				if (room[i][j] == 'x' || room[i][j] == '.')
					continue;

				if (room[i][j] == 'o')
					pos = vertex_size;
				dirty.push({ i, j });
				room[i][j] = vertex_size;
				vertex_size++;
			}
		}

		int ii = 0;
		// 정점 사이의 거리 탐색
		while (!dirty.empty()) {
			queue<P> q;
			P cur;

			int visited[20][20] = { 0, };
			int dx[4] = { -1, 1, 0, 0 };
			int dy[4] = { 0, 0, -1, 1 };

			cur = dirty.front(); dirty.pop();
			q.push(cur);
			visited[cur.x][cur.y] = 1;

			// BFS
			while (!q.empty()) {
				cur = q.front(); q.pop();

				if (0 <= room[cur.x][cur.y] && room[cur.x][cur.y] <= 10)
					edge[ii][room[cur.x][cur.y]] = visited[cur.x][cur.y] - 1;

				for (int dir = 0; dir < 4; dir++) {
					P np = { cur.x + dx[dir], cur.y + dy[dir] };

					if (np.x < 0 || np.x >= h || np.y < 0 || np.y >= w)
						continue;
					if (visited[np.x][np.y])
						continue;
					if (room[np.x][np.y] == 'x')
						continue;

					q.push(np);
					visited[np.x][np.y] = visited[cur.x][cur.y] + 1;
				}
			}

			ii++;
		}

		bool is = true;
		for (int i = 0; i < vertex_size; i++) {
			for (int j = 0; j < vertex_size; j++) {
				if (i != j && !edge[i][j]) {
					is = false;
					break;
				}
			}
			if (!is) {
				break;
			}
		}
		if (!is) {
			printf("-1\n");
			continue;
		}

		ans = INT_MAX;
		ind = 0;
		current = 0;
		vertex[pos] = 1;
		
		r();

		printf("%d\n", ans);
	}
}