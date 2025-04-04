#include <iostream>
#include <cstdlib> // abs()

using namespace std;

int n, m;
int b[10] = { 0, };
int c = 100;

inline int diff(int channel) {
	return abs(channel - n);
}

int nearest_channel = 1000000;
int nearest_count = 1000000;

void get_nearest_channel(int channel = 0, int btn_count = 0) {
	if (btn_count) {
		if (diff(channel) < diff(nearest_channel)) {
			nearest_channel = channel;
			nearest_count = btn_count;
		}
		else if (diff(channel) == diff(nearest_channel)) {
			if (btn_count < nearest_count) {
				nearest_channel = channel;
				nearest_count = btn_count;
			}
		}
		else {
			if (channel > n)
				return;
		}
	}

	for (int i = 0; i < 10; i++) {
		if (b[i])
			continue;

		if (i || channel || !btn_count) {
			get_nearest_channel(channel * 10 + i, btn_count + 1);
		}
	}
}

int main() {
	cin >> n;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int temp;
		cin >> temp;

		b[temp] = 1;
	}

	get_nearest_channel();

	if (diff(nearest_channel) + nearest_count < diff(100))
		cout << diff(nearest_channel) + nearest_count << endl;
	else
		cout << diff(100);
}