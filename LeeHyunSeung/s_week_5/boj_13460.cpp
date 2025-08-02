#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

struct ball { int x; int y; };
struct unit { ball red, blue; int last_dir; int index; };

char board[10][11];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

// dir - 0: 위쪽 / 1: 오른쪽 / 2: 아래쪽 / 3: 왼쪽
ball move(int dir, ball a, ball b = { -1, -1 }) {
	while (board[a.x + dx[dir]][a.y + dy[dir]] == '.' && !(a.x + dx[dir] == b.x && a.y + dy[dir] == b.y))
		a = { a.x + dx[dir], a.y + dy[dir] };
	if (board[a.x + dx[dir]][a.y + dy[dir]] == 'O')
		return { -1, -1 };
	return a;
}

int main() {
	int n, m;
	ball red, blue;

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%s", board[i]);

		for (int j = 0; j < m; j++) {
			if (board[i][j] == 'R') {
				red = { i, j };
				board[i][j] = '.';
			}
			if (board[i][j] == 'B') {
				blue = { i, j };
				board[i][j] = '.';
			}
		}
	}

	queue<unit> q;
	unit cur;

	int ans = 999;
	
	// 4방향 탐색
	for (int i = 0; i < 4; i++) {
		ball nr, nb;

		if (red.x * dx[i] > blue.x * dx[i] || red.y * dy[i] > blue.y * dy[i]) {
			nr = move(i, red);
			nb = move(i, blue, nr);
		}
		else {
			nb = move(i, blue);
			nr = move(i, red, nb);
		}

		q.push({nr, nb, i, 1});
	}

	while (!q.empty()) {
		cur = q.front(); q.pop();

		if (cur.red.x == -1) {
			if (cur.blue.x == -1)
				continue;

			if (cur.index < ans) {
				ans = cur.index;
				continue;
			}
		}

		if (cur.index == 10)
			continue;

		ball nr, nb;
		int dir;

		dir = (cur.last_dir + 1) % 4;
		if (cur.red.x * dx[dir] > cur.blue.x * dx[dir] || cur.red.y * dy[dir] > cur.blue.y * dy[dir]) {
			nr = move(dir, cur.red);
			nb = move(dir, cur.blue, nr);
		}
		else {
			nb = move(dir, cur.blue);
			nr = move(dir, cur.red, nb);
		}
		q.push({ nr, nb, dir, cur.index + 1 });

		dir = (cur.last_dir + 3) % 4;
		if (cur.red.x * dx[dir] > cur.blue.x * dx[dir] || cur.red.y * dy[dir] > cur.blue.y * dy[dir]) {
			nr = move(dir, cur.red);
			nb = move(dir, cur.blue, nr);
		}
		else {
			nb = move(dir, cur.blue);
			nr = move(dir, cur.red, nb);
		}
		q.push({ nr, nb, dir, cur.index + 1 });
	}

	if (ans == 999)
		printf("-1\n");
	else
		printf("%d\n", ans);
}
