#include <iostream>
#include <queue>

using namespace std;

char map[101] = { 0, };
char memo[101] = { 0, };

int main() {
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n + m; i++) {
		int x, y;
		cin >> x >> y;
		map[x] = y;
	}

	queue<int> q;
	q.push(1);

	while (!q.empty()) {
		int cur = q.front(); q.pop();

		if (cur == 100)
			break;

		for (int dir = 1; dir <= 6; dir++) {
			int n_cur = cur + dir;

			if (memo[n_cur])
				continue;

			memo[n_cur] = memo[cur] + 1;

			int nn_cur;
			if (map[n_cur]) {
				nn_cur = map[n_cur];

				if (memo[nn_cur])
					continue;

				memo[nn_cur] = memo[cur] + 1;
				q.push(nn_cur);
			}
			else {
				q.push(n_cur);
			}
		}
	}

	cout << (int)memo[100] << endl;
}