#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

struct P { int x; int y; };

char board[50][51];
int visited[50][50];

int main() {
	int n;
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%s", board[i]);
	}

	memset(visited, -1, sizeof(visited));

	queue<P> q;
	P cur;

	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };

	q.push({ 0, 0 });
	visited[0][0] = 0;

	while (!q.empty()) {
		cur = q.front(); q.pop();
		for (int dir = 0; dir < 4; dir++) {
			P n_cur = { cur.x + dx[dir], cur.y + dy[dir] };

			if (n_cur.x < 0 || n_cur.x >= n || n_cur.y < 0 || n_cur.y >= n)
				continue;

			int value = visited[cur.x][cur.y];
			if (board[n_cur.x][n_cur.y] == '0')
				value++;

			if (visited[n_cur.x][n_cur.y] >= 0 && value >= visited[n_cur.x][n_cur.y])
				continue;

			q.push(n_cur);
			visited[n_cur.x][n_cur.y] = value;
		}
	}

	printf("%d\n", visited[n - 1][n - 1]);
}