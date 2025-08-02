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

		vector<vector<int>> temp;
		for (int dir = 0; dir < 4; dir++) {
			temp = cur.first;

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
				for (int j = 0; j < n; j++) {
					cur.first[i][j] = temp[j][(n - 1) - i];
				}
			}
		}
	}

	cout << ans << endl;
}