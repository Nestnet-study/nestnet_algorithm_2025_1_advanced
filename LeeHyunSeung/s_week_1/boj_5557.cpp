#include <cstdio>

using namespace std;

long long int memo[99][21] = { 0, };

int main() {
	int n;
	int arr[100] = { 0, };

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	memo[0][arr[0]] = 1;
	for (int i = 1; i < n - 1; i++) {
		for (int j = 0; j <= 20; j++) {
			if (!memo[i - 1][j])
				continue;

			int plus = j + arr[i];
			if (0 <= plus && plus <= 20) {
				memo[i][plus] += memo[i - 1][j];
			}
			
			int minus = j - arr[i];
			if (0 <= minus && minus <= 20) {
				memo[i][minus] += memo[i - 1][j];
			}
		}
	}

	printf("%lld\n", memo[n - 2][arr[n - 1]]);
}