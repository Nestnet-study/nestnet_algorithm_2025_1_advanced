#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct date { int month; int day; };

// flower 정렬 비교 함수 - 개화일 오름차순
bool Greater(pair<date, date> a, pair<date, date> b) {
	if (a.first.month == b.first.month) {
		return a.first.day < b.first.day;
	}
	else {
		return a.first.month < b.first.month;
	}
}

// a의 날짜가 b의 날짜보다 작거나 같은지 확인
inline bool CompareDate(date a, date b) {
	return a.month < b.month || (a.month == b.month && a.day <= b.day);
}

vector<pair<date, date>> flower;

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		flower.push_back({ {a, b}, {c, d} });
	}

	sort(flower.begin(), flower.end(), Greater);

	date latest = { 3, 1 };
	int count = 0;
	int index = 0;
	while (latest.month < 12) {
		date select_end = { 1, 1 };
		bool selected = false;

		while (index < n && CompareDate(flower[index].first, latest)) {
			if (CompareDate(select_end, flower[index].second)) {
				select_end = flower[index].second;
				selected = true;
			}
			index++;
		}

		if (!selected) {
			count = -1;
			break;
		}
		
		latest = select_end;
		count++;
	}

	if (count == -1) {
		cout << 0 << endl;
	}
	else {
		cout << count << endl;
	}
}