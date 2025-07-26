#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

// 각 원소가 어느 집합에 속해 있는지 저장
int facebook[1000000] = { 0, };
// 각 집합에 어느 원소가 속해 있는지 저장
vector<int> where[1000001];

int main() {
	int test;

	scanf("%d", &test);

	for (int t = 1; t <= test; t++) {
		// 초기화
		for (int i = 0; i < 1000001; i++) {
			where[i] = vector<int>();
		}
		memset(facebook, 0, sizeof(facebook));

		// 입력
		int n, k, m;
		int x, y;

		scanf("%d", &n);
		scanf("%d", &k);

		int index = 1;

		for (int i = 0; i < k; i++) {
			scanf("%d %d", &x, &y);

			// 둘 다 그룹이 없다
			if (!facebook[x] && !facebook[y]) {
				facebook[x] = index;
				facebook[y] = index;

				where[index].push_back(x);
				where[index].push_back(y);

				index++;
			}
			// x가 그룹이 없다
			else if (!facebook[x]) {
				facebook[x] = facebook[y];
				where[facebook[y]].push_back(x);
			}
			// y가 그룹이 없다
			else if (!facebook[y]) {
				facebook[y] = facebook[x];
				where[facebook[x]].push_back(y);
			}
			// 둘 다 그룹이 있다 - 서로 다르다
			else {
				if (facebook[x] != facebook[y]) {
					int change = facebook[y];
					
					for (int j = 0; j < where[change].size(); j++) {
						facebook[where[change][j]] = facebook[x];
						where[facebook[x]].push_back(where[change][j]);
					}
					where[change] = vector<int>();
				}
			}
		}

		// 확인
		scanf("%d", &m);

		printf("Scenario %d:\n", t);
		for (int i = 0; i < m; i++) {
			scanf("%d %d", &x, &y);

			if (x == y || (facebook[x] && facebook[y] && facebook[x] == facebook[y])) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}

		printf("\n");
	}
}