/*
# 규칙
0: 중앙, 1: 위, 2: 왼, 3: 아래, 4: 오
두 발이 같은 지점에 올 수 없다. (게임 시작 시에는 예외)
중앙의 발이 다른 지점으로 움직일 때:                         힘 2 소모
다른 지점에서 인접한 지점으로 움직일 때 (e.g. 위 -> 왼, 오): 힘 3 소모
반대편으로 움직일 때 (e.g. 위 -> 아래):                      힘 4 소모
같은 지점을 한 번 더 누를 때:                                힘 1 소모
*/

#include <cstdio>
#include <climits>

using namespace std;

inline int get_require(int from, int to) {
	if (from == to)
		return 1;
	else if (from == 0)
		return 2;
	else if (from - to == 2 || to - from == 2)
		return 4;
	else
		return 3;
}

struct REQ {
	int left;
	int right;
} require;

int main() {
	bool feet[5][5] = { false, };

	int ans[5][5] = { 0, };

	int move;
	bool is_first = true;
	while (1) {
		scanf("%d", &move);

		if (!move)
			break;

		if (is_first) {
			feet[move][0] = true;
			ans[move][0] = get_require(0, move);
			is_first = false;

			continue;
		}

		bool temp_feet[5][5] = { false, };
		int temp_ans[5][5] = { 0, };

		for (int left = 0; left < 5; left++) {
			for (int right = 0; right < 5; right++) {
				if (!feet[left][right])
					continue;

				if (right != move) {
					require.left = get_require(left, move);

					temp_feet[move][right] = true;

					if (!temp_ans[move][right] || ans[left][right] + require.left < temp_ans[move][right])
						temp_ans[move][right] = ans[left][right] + require.left;
				}
				if (left != move) {
					require.right = get_require(right, move);

					temp_feet[left][move] = true;

					if (!temp_ans[left][move] || ans[left][right] + require.right < temp_ans[left][move])
						temp_ans[left][move] = ans[left][right] + require.right;
				}
			}
		}
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				ans[i][j] = temp_ans[i][j];
				feet[i][j] = temp_feet[i][j];
			}
		}
	}
	int min_ans = INT_MAX;
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			if (ans[i][j] && ans[i][j] < min_ans)
				min_ans = ans[i][j];
		}
	}

	if (min_ans == INT_MAX)
		printf("0\n");
	else 
		printf("%d\n", min_ans);
}