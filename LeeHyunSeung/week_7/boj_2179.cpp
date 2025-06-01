#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct word {
	int num; // 단어의 원래 입력 순서
	string word; // 단어 문자열
};
struct w_index {
	vector<int> index;
	int similarity;
};

vector<word> v;
vector<string> v_t;
vector<w_index> w_i;

int greater_word(word a, word b) { return a.word < b.word; }
int greater_index(w_index a, w_index b) {
	if (a.similarity == b.similarity) {
		return a.index[0] < b.index[0];
	}
	else return a.similarity > b.similarity;
}

int testtest(pair<int, int> a, pair<int, int> b) { return a.second < b.second; };
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		v.push_back({ i, s });
		v_t.push_back(s);

	}

	sort(v.begin(), v.end(), greater_word);

	int s_index = -1;
	int last = -1;
	for (int i = 0; i < n - 1; i++) {
		int similarity = 0;
		for (int j = 0; j < min(v[i].word.size(), v[i + 1].word.size()); j++) {
			if (v[i].word[j] != v[i + 1].word[j])
				break;
			similarity++;

		}
		
		if (!i || similarity != last) {
			s_index++; 
			last = similarity;
			w_i.push_back({ { v[i].num, v[i + 1].num }, similarity });
		}
		else {
			w_i[s_index].index.push_back(v[i + 1].num);
		}
	}

	for (int i = 0; i < w_i.size(); i++) {
		sort(w_i[i].index.begin(), w_i[i].index.end());
	}

	sort(w_i.begin(), w_i.end(), greater_index);

	cout << v_t[w_i[0].index[0]] << "\n" << v_t[w_i[0].index[1]];
}