#include <cstdio>
#include <queue>

using namespace std;

struct P { int x; int y; };

char board[100][101];
char word[81];

long long int visited[80][100][100];

int main() {
	int n, m, k;
	int length;

	// 입력
	scanf("%d %d %d", &n, &m, &k);
	
	for (int i = 0; i < n; i++) {
		scanf("%s", board[i]);
	}

	scanf("%s", word);

	// 첫 글자 찾기
	queue<P> q;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (board[i][j] == word[0]) {
				visited[0][i][j] = 1;
				q.push({ i, j });
			}
		}
	}

	// 경우의 수 탐색
	P cur;

	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };

	for (int i = 1; i <= 80; i++) {
		if (word[i] == '\0') {
			length = i;
			break;
		}

		queue<P> temp;

		while (!q.empty()) {
			cur = q.front(); q.pop();

			for (int dir = 0; dir < 4; dir++) {
				for (int mul = 1; mul <= k; mul++) {
					int nx = cur.x + dx[dir] * mul;
					int ny = cur.y + dy[dir] * mul;

					if (nx < 0 || nx >= n || ny < 0 || ny >= m)
						break;

					if (board[nx][ny] == word[i]) {
						if (!visited[i][nx][ny]) {
							temp.push({ nx, ny });
						}
						visited[i][nx][ny] += visited[i - 1][cur.x][cur.y];
					}
				}
			}
		}
		q = temp;
	}

	// 정답 출력
	long long int ans = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			ans += visited[length - 1][i][j];
		}
	}

	printf("%d\n", ans);
}