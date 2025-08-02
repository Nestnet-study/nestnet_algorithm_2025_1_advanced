#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>

using namespace std;

vector<vector<int>> board(20);

int n;
int ans = 0;

vector<vector<int>> move;

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		board[i] = vector<int>(20);

		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
		}
	}

	stack<pair<vector<vector<int>>, int>> s;
	pair<vector<vector<int>>, int> cur;

	s.push({ board, 0 });

	while (!s.empty()) {
		cur = s.top(); s.pop();

		if (cur.second == 5)
			continue;

		vector<vector<int>> temp = cur.first;
		for (int i = 0; i < n; i++) {
			int index = 0;
			bool is_merged = false;
			for (int j = 0; j < n; j++) {
				if (!temp[i][j])
					continue;

				if (!is_merged && index && temp[i][index - 1] == temp[i][j]) {
					temp[i][index - 1] *= 2;
					is_merged = true;
				}
				else {
					temp[i][index] = temp[i][j];
					is_merged = false;
					index++;
				}

				if (temp[i][index - 1] > ans)
					ans = temp[i][index - 1];
			}
			for (int j = index; j < n; j++) {
				temp[i][j] = 0;
			}
		}

		s.push({ temp, cur.second + 1 });

		temp = cur.first;
		for (int i = 0; i < n; i++) {
			int index = 0;
			bool is_merged = false;
			for (int j = 0; j < n; j++) {
				if (!temp[i][(n - 1) - j])
					continue;

				if (!is_merged && index && temp[i][(n - 1) - (index - 1)] == temp[i][(n - 1) - j]) {
					temp[i][(n - 1) - (index - 1)] *= 2;
					is_merged = true;
				}
				else {
					temp[i][(n - 1) - index] = temp[i][(n - 1) - j];
					is_merged = false;
					index++;
				}

				if (temp[i][(n - 1) - (index - 1)] > ans)
					ans = temp[i][(n - 1) - (index - 1)];
			}
			for (int j = index; j < n; j++) {
				temp[i][(n - 1) - j] = 0;
			}
		}

		s.push({ temp, cur.second + 1 });

		temp = cur.first;
		for (int i = 0; i < n; i++) {
			int index = 0;
			bool is_merged = false;
			for (int j = 0; j < n; j++) {
				if (!temp[j][i])
					continue;

				if (!is_merged && index && temp[index - 1][i] == temp[j][i]) {
					temp[index - 1][i] *= 2;
					is_merged = true;
				}
				else {
					temp[index][i] = temp[j][i];
					is_merged = false;
					index++;
				}

				if (temp[index - 1][i] > ans)
					ans = temp[index - 1][i];
			}
			for (int j = index; j < n; j++) {
				temp[j][i] = 0;
			}
		}

		s.push({ temp, cur.second + 1 });

		temp = cur.first;
		for (int i = 0; i < n; i++) {
			int index = 0;
			bool is_merged = false;
			for (int j = 0; j < n; j++) {
				if (!temp[(n - 1) - j][i])
					continue;

				if (!is_merged && index && temp[(n - 1) - (index - 1)][i] == temp[(n - 1) - j][i]) {
					temp[(n - 1) - (index - 1)][i] *= 2;
					is_merged = true;
				}
				else {
					temp[(n - 1) - index][i] = temp[(n - 1) - j][i];
					is_merged = false;
					index++;
				}

				if (temp[(n - 1) - (index - 1)][i] > ans)
					ans = temp[(n - 1) - (index - 1)][i];
			}
			for (int j = index; j < n; j++) {
				temp[(n - 1) - j][i] = 0;
			}
		}

		s.push({ temp, cur.second + 1 });
	}

	cout << ans << endl;
}