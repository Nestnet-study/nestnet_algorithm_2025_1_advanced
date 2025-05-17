#include <cstdio>
#include <climits>
#include <cstring>

using namespace std;

int arr[200][200];
int sum[200][200];

int main() {
	int n, m;
	int ans = INT_MIN;
	
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &arr[i][j]);
		}
	}

	memset(sum, -1, sizeof(sum));

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			for (int i = x; i < n; i++) {
				for (int j = y; j < m; j++) {
					sum[i][j] = arr[i][j];
					if (i > x)
						sum[i][j] += sum[i - 1][j];
					if (j > y)
						sum[i][j] += sum[i][j - 1];
					if (i > x && j > y)
						sum[i][j] -= sum[i - 1][j - 1];

					if (sum[i][j] > ans) ans = sum[i][j];
				}
			}
		}
	}

	printf("%d\n", ans);
}