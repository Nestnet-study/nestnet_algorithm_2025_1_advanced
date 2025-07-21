#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int emo[2000][2000];

int main() {
	int s;

	scanf("%d", &s);

	memset(emo, -1, sizeof(emo));

	queue<pair<int, int>> q;
	pair<int, int> cur;

	int greatest_copy = 0;

	q.push({ 1, 0 });
	emo[1][0] = 0;

	while (!q.empty()) {
		cur = q.front(); q.pop();

		if (cur.first >= s)
			continue;

		// 복사
		if (emo[cur.first][cur.first] == -1 || emo[cur.first][cur.second] + 1 < emo[cur.first][cur.first]) {
			q.push({ cur.first, cur.first });
			emo[cur.first][cur.first] = emo[cur.first][cur.second] + 1;

			if (greatest_copy < cur.first)
				greatest_copy = cur.first;
		}
		
		// 붙여넣기
		if (cur.second) {
			if (emo[cur.first + cur.second][cur.second] == -1 || emo[cur.first][cur.second] + 1 < emo[cur.first + cur.second][cur.second]) {
				q.push({ cur.first + cur.second, cur.second });
				emo[cur.first + cur.second][cur.second] = emo[cur.first][cur.second] + 1;
			}
		}

		// 1개 지우기
		if (cur.first) {
			if (emo[cur.first - 1][cur.second] == -1 || emo[cur.first][cur.second] + 1 < emo[cur.first - 1][cur.second]) {
				q.push({ cur.first - 1, cur.second });
				emo[cur.first - 1][cur.second] = emo[cur.first][cur.second] + 1;
			}
		}
	}

	int ans = 99999;
	for (int i = 0; i <= greatest_copy; i++) {
		if (emo[s][i] > 0 && emo[s][i] < ans)
			ans = emo[s][i];
	}

	printf("%d\n", ans);
}