#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

inline int calc(int a, char op, int b) {
	switch (op) {
	case '*':
		return a * b;
	case '+':
		return a + b;
	case '-':
		return a - b;
	}
}

char road[5][6];
int greater_step[5][5];
int lesser_step[5][5];

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> road[i][j];
		}
	}

	// 첫 번째 칸
	greater_step[0][0] = road[0][0] - '0';
	// 첫 번째 줄 (가로, 세로)
	for (int i = 1; i < n; i++) {
		if (i % 2 == 0) {
			greater_step[0][i] = calc(greater_step[0][i - 1], road[0][i - 1], road[0][i] - '0');
			greater_step[i][0] = calc(greater_step[i - 1][0], road[i - 1][0], road[i][0] - '0');

			lesser_step[0][i] = calc(greater_step[0][i - 1], road[0][i - 1], road[0][i] - '0');
			lesser_step[i][0] = calc(greater_step[i - 1][0], road[i - 1][0], road[i][0] - '0');
		}
		else {
			greater_step[0][i] = greater_step[0][i - 1];
			greater_step[i][0] = greater_step[i - 1][0];

			lesser_step[0][i] = greater_step[0][i - 1];
			lesser_step[i][0] = greater_step[i - 1][0];
		}
	}
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if ((i + j) % 2 == 0) {
				greater_step[i][j] = max(
					calc(greater_step[i - 1][j], road[i - 1][j], road[i][j] - '0'),
					calc(greater_step[i][j - 1], road[i][j - 1], road[i][j] - '0')
				);

				lesser_step[i][j] = min(
					calc(lesser_step[i - 1][j], road[i - 1][j], road[i][j] - '0'),
					calc(lesser_step[i][j - 1], road[i][j - 1], road[i][j] - '0')
				);
			}
			else {
				greater_step[i][j] = max(greater_step[i - 1][j], greater_step[i][j - 1]);

				lesser_step[i][j] = min(lesser_step[i - 1][j], lesser_step[i][j - 1]);
			}
		}
	}
	
	printf("%d %d\n", greater_step[n - 1][n - 1], lesser_step[n - 1][n - 1]);
}