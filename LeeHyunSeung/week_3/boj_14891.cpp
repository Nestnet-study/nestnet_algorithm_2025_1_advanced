#include <cstdio>

using namespace std;

int cog[4][8];

// from: { -1: 왼쪽에서, 0: 자신, 1: 오른쪽에서 }
void turn_cog(int index, int dir, int from) {
	if (from <= 0 && index + 1 < 4) {
		if (cog[index][2] != cog[index + 1][6]) {
			turn_cog(index + 1, dir == 1 ? -1 : 1, -1);
		}
	}
	if (from >= 0 && index > 0) {
		if (cog[index][6] != cog[index - 1][2]) {
			turn_cog(index - 1, dir == 1 ? -1 : 1, 1);
		}
	}

	int temp;
	if (dir == 1) {
		temp = cog[index][7];
		for (int i = 7; i > 0; i--) {
			cog[index][i] = cog[index][i - 1];
		}
		cog[index][0] = temp;
	}
	else {
		temp = cog[index][0];
		for (int i = 0; i < 7; i++) {
			cog[index][i] = cog[index][i + 1];
		}
		cog[index][7] = temp;
	}
}

int main() {
	for (int i = 0; i < 4; i++) {
		char in[9];
		scanf("%s", in);
		for (int j = 0; j < 8; j++)
			cog[i][j] = in[j] - 48;
	}

	int k;
	int num, dir;
	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		scanf("%d %d", &num, &dir);

		turn_cog(num - 1, dir, 0);
	}

	printf("%d\n", cog[0][0] + cog[1][0] * 2 + cog[2][0] * 4 + cog[3][0] * 8);
}