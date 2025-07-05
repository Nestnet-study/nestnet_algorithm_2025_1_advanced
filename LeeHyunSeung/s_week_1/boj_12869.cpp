#include <cstdio>
#include <queue>

using namespace std;

char health[61][61][61] = { 0, };

struct SCV { int a; int b; int c; };

int main() {
	int n;
	int arr[3] = { 0, };

	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	queue<SCV> q;
	SCV cur;

	int dir[6][3] = {
		{ 9, 3, 1 },
		{ 9, 1, 3 },
		{ 3, 9, 1 },
		{ 3, 1, 9 },
		{ 1, 9, 3 },
		{ 1, 3, 9 }
	};

	q.push({ arr[0], arr[1], arr[2] });
	
	while (!q.empty()) {
		cur = q.front(); q.pop();

		for (int d = 0; d < 6; d++) {
			int nx = cur.a - dir[d][0];
			int ny = cur.b - dir[d][1];
			int nz = cur.c - dir[d][2];

			if (nx < 0) nx = 0;
			if (ny < 0) ny = 0;
			if (nz < 0) nz = 0;

			int value = health[cur.a][cur.b][cur.c] + 1;
			if (!health[nx][ny][nz] || value < health[nx][ny][nz]) {
				q.push({ nx, ny, nz });
				health[nx][ny][nz] = value;
			}
		}
	}

	printf("%d\n", health[0][0][0]);
}