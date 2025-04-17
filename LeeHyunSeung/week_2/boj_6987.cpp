#include <iostream>

using namespace std;

int w[6], d[6], l[6];
bool is_possible;

bool is_five() {
	for (int i = 0; i < 6; i++) {
		if (w[i] + d[i] + l[i] != 5)
			return false;
	}
	return true;
}

void dfs(int home, int away) {
	if (is_possible)
		return;

	if (away == 6) {
		home++;
		away = home + 1;
	}
	if (home == 5) {
		is_possible = true;
		return;
	}

	if (w[home] && l[away]) {
		w[home]--; l[away]--;
		dfs(home, away + 1);
		w[home]++; l[away]++;
	}
	if (d[home] && d[away]) {
		d[home]--; d[away]--;
		dfs(home, away + 1);
		d[home]++; d[away]++;
	}
	if (l[home] && w[away]) {
		l[home]--; w[away]--;
		dfs(home, away + 1);
		l[home]++; w[away]++;
	}
}

int main() {
	for (int t = 0; t < 4; t++)
	{
		for (int i = 0; i < 6; i++) {
			cin >> w[i];
			cin >> d[i];
			cin >> l[i];
		}

		is_possible = false;

		if (is_five()) {
			dfs(0, 1);
			if (is_possible)
				cout << "1 ";
			else
				cout << "0 ";
		}
		else {
			cout << "0 ";
		}
	}
}