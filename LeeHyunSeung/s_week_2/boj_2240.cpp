#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int plum[1000];
int p_sum[1000];
int visited[1050][31];

struct P { int t; int w; };

int main() {
	// 입력
	int t, w;
	
	scanf("%d %d", &t, &w);

	for (int i = 0; i < t; i++) {
		scanf("%d", &plum[i]);
	}

	// 연속된 자두 합치기
	int p_size = 0;
	int prev = plum[0];

	if (plum[0] == 2) p_size++;
	
	for (int i = 0; i < t; i++) {
		if (plum[i] != prev) {
			prev = plum[i];
			p_size += 1;
		}
		p_sum[p_size]++;
	}
	// p_sum[0, p_size]

	// 탐색
	memset(visited, -1, sizeof(visited));

	queue<P> q;
	P cur;

	q.push({ 0, w });
	visited[0][w] = p_sum[0];

	while (!q.empty()) {
		cur = q.front(); q.pop();

		if (cur.t == p_size)
			continue;

		int value;

		// 위치 이동
		if (cur.w) {
			value = visited[cur.t][cur.w] + p_sum[cur.t + 1];

			if (value > visited[cur.t + 1][cur.w - 1]) {
				q.push({ cur.t + 1, cur.w - 1 });
				visited[cur.t + 1][cur.w - 1] = value;
			}
		}

		// 가만히 있기
		int pos = min(cur.t + 2, p_size);
		value = visited[cur.t][cur.w] + p_sum[cur.t + 2];

		if (value > visited[pos][cur.w] < value) {
			q.push({ pos, cur.w });
			visited[pos][cur.w] = value;
		}
	}

	/*printf("\n");
	for (int i = 0; i <= p_size; i++) {
		for (int j = 0; j <= w; j++) {
			printf("%d ", visited[i][j]);
		}
		printf("\n");
	}
	printf("\n");*/

	int ans = 0;
	for (int i = 0; i <= w; i++) {
		if (ans < visited[p_size][i]) {
			ans = visited[p_size][i];
		}
	}

	printf("%d\n", ans);
}