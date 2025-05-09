#include <iostream>
#include <vector>
#include <cstring>

#define INF 987654321;

using namespace std;

vector<int> v_pos;
int dp_table[100001][5][5];

// 이동일 때, 드는 힘 계산하는 함수
int dist(int cur, int next)
{
	if (cur == 0) return 2;	// 0의 위치에서 이동할 때
	if (cur == next) return 1;	// 동일한 위치로 이동할 때
	if (abs(cur - next) == 2) return 4;	// 반대편으로 이동할 때
	return 3;	// 인접한 위치로 이동할 때
}

// 다이나믹 프로그래밍을 통한 계산
int dp(int cur, int left, int right)
{
	int v_size = v_pos.size();
	if (cur == v_size - 1) return 0;	// 0에서 시작

	// memoization 기록(속도 향상용)
	if (dp_table[cur][left][right] != -1) return dp_table[cur][left][right];

	int left_val = dp(cur + 1, v_pos[cur + 1], right) + dist(left, v_pos[cur + 1]);	// 왼쪽 발이 움직였을 경우
	int right_val = dp(cur + 1, left, v_pos[cur + 1]) + dist(right, v_pos[cur + 1]);	// 오른쪽 발이 움직였을 경우

	return dp_table[cur][left][right] = min(left_val, right_val);	// 왼쪽 발과 오른쪽 발로 움직였을 경우 중에서 가장 작은 값
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	// 초기화
	memset(dp_table, -1, sizeof(dp_table));

	// 0의 위치에서 시작
	v_pos.push_back(0);

	// 0이 나올 때 까지 위치 계속 입력 받기
	while (true)
	{
		int pos;
		cin >> pos;

		if (pos == 0) break;	// 0이면 종료
		v_pos.push_back(pos);
	}

	cout << dp(0, 0, 0);

	return 0;
}