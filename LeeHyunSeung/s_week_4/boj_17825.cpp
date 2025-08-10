#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

// 각 칸의 점수
int score[33] = {
	0,
	2, 4, 6, 8, 10,
	12, 14, 16, 18, 20,
	22, 24, 26, 28, 30,
	32, 34, 36, 38, 40,
	13, 16, 19,
	22, 24,
	28, 27, 26,
	25,
	30, 35,
	0
};
// 각 칸의 다음 칸 (빨간색 화살표)
// (예외: 5 -> 21, 10 -> 24, 15 -> 26)
int map[33] = {
	1,
	2, 3, 4, 5, 6,
	7, 8, 9, 10, 11,
	12, 13, 14, 15, 16,
	17, 18, 19, 20, 32,
	22, 23, 29,
	25, 29,
	27, 28, 29,
	30,
	31, 20,
};
// 특수 이동 칸
int special[33];

short visited[11][33][33][33][33];

int main() {
	// 입력
	int move[10];

	for (int i = 0; i < 10; i++) {
		scanf("%d", &move[i]);
	}

	// 특수 이동 칸 지정
	special[5] = 21;
	special[10] = 24;
	special[15] = 26;
	
	// first: 회차, second: 말의 위치 (정렬)
	queue<pair<int, vector<int>>> q;
	pair<int, vector<int>> cur;

	int ans = 0;

	q.push({ 0, {0, 0, 0, 0} });
	visited[0][0][0][0][0] = 0;

	while (!q.empty()) {
		cur = q.front(); q.pop();

		if (cur.first == 10) {
			if (ans < visited[10][cur.second[0]][cur.second[1]][cur.second[2]][cur.second[3]]) {
				ans = visited[10][cur.second[0]][cur.second[1]][cur.second[2]][cur.second[3]];
			}
			continue;
		}

		// 4개의 말 모두 이동시켜보기
		int move_amount = move[cur.first];

		for (int i = 0; i < 4; i++) {
			// 이동
			vector<int> nx = cur.second;
			int new_score = visited[cur.first][nx[0]][nx[1]][nx[2]][nx[3]];

			if (nx[i] == 32)
				continue;
			if (special[nx[i]]) {
				nx[i] = special[nx[i]];
				for (int j = 1; j < move_amount; j++) {
					nx[i] = map[nx[i]]; 
					if (nx[i] == 32)
						break;
				}
			}
			else {
				for (int j = 0; j < move_amount; j++) {
					nx[i] = map[nx[i]];
					if (nx[i] == 32)
						break;
				}
			}

			// 유효한 갈래인지 확인
			bool is_wrong = false;
			if (nx[i] != 32) {
				for (int j = 0; j < 4; j++) {
					if (j == i)
						continue;

					if (nx[i] == nx[j]) {
						is_wrong = true;
						break;
					}
				}
				if (is_wrong)
					continue;
			}

			new_score += score[nx[i]];

			sort(nx.begin(), nx.end());

			if (new_score > visited[cur.first + 1][nx[0]][nx[1]][nx[2]][nx[3]]) {
				q.push({ cur.first + 1, nx });
				visited[cur.first + 1][nx[0]][nx[1]][nx[2]][nx[3]] = new_score;
			}
		}
	}

	printf("%d\n", ans);
}