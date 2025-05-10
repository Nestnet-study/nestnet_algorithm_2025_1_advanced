#include <cstdio>

using namespace std;

int arr[100000];
int p_sum[100000];

int main() {
	int n, s;

	scanf("%d %d", &n, &s);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	// 부분합 구하기
	p_sum[0] = arr[0];
	for (int i = 1; i < n; i++) {
		p_sum[i] = arr[i] + p_sum[i - 1];
	}

	int ans = 100001;
	for (int sum_index = 0, sub_index = 0; sum_index < n; sum_index++) {
		if (p_sum[sum_index] < s)
			continue;

		while (p_sum[sum_index] - p_sum[sub_index] >= s)
			sub_index++;

		if (sum_index - sub_index + 1 < ans)
			ans = sum_index - sub_index + 1;
	}

	if (ans == 100001)
		printf("0\n");
	else
		printf("%d\n", ans);
}