#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

char board[100][100];

int main() {
	int n, k, l;

	cin >> n;
	cin >> k;
	
	for (int i = 0; i < k; i++) {
		int x, y;
		cin >> x >> y;
		board[x - 1][y - 1] = '@';
	}

	pair<int, char> ctrl[100];
	int ctrl_index = 0;

	cin >> l;

	for (int i = 0; i < l; i++) {
		int x;
		char c;
		cin >> x >> c;
		ctrl[ctrl_index++] = { x, c };
	}

	deque<pair<int, int>> snake;
	int dir = 0;

	int dx[4] = { 0, 1, 0, -1 };
	int dy[4] = { 1, 0, -1, 0 };

	board[0][0] = '#';
	snake.push_front({ 0, 0 });

	ctrl_index = 0;

	int time_index;
	for (time_index = 0; time_index < 15000; time_index++) {
		if (ctrl_index < l && time_index == ctrl[ctrl_index].first) {
			if (ctrl[ctrl_index].second == 'L') {
				dir = (dir + 3) % 4;
			}
			else {
				dir = (dir + 1) % 4;
			}

			ctrl_index++;
		}

		int nx = snake.front().first + dx[dir];
		int ny = snake.front().second + dy[dir];

		if (nx < 0 || nx >= n || ny < 0 || ny >= n)
			break;
		if (board[nx][ny] == '#')
			break;

		snake.push_front({ nx, ny });

		if (!board[nx][ny]) {
			board[snake.back().first][snake.back().second] = 0;
			snake.pop_back();
		}

		board[nx][ny] = '#';
	}

	cout << time_index + 1 << endl;
}