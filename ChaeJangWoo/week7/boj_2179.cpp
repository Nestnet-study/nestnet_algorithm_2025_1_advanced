#include <iostream>
#include <string>
#include <vector>
using namespace std;

// 접두사 길이 계산 함수
int getCommonPrefixLength(const string& a, const string& b) {
    int len = min(a.size(), b.size());
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (a[i] != b[i]) break;
        count++;
    }
    return count;
}

int main() {
    int n;
    cin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    int maxPrefix = 0;
    int firstIndex = -1;
    int secondIndex = -1;

    // 모든 쌍 비교
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (words[i] == words[j]) continue;

            int prefixLen = getCommonPrefixLength(words[i], words[j]);

            if (prefixLen > maxPrefix ||
               (prefixLen == maxPrefix && 
               (i < firstIndex || (i == firstIndex && j < secondIndex)))) {
                maxPrefix = prefixLen;
                firstIndex = i;
                secondIndex = j;
            }
        }
    }

    // 입력 순서 보장
    if (firstIndex > secondIndex) swap(firstIndex, secondIndex);

    cout << words[firstIndex] << '\n';
    cout << words[secondIndex] << '\n';

    return 0;
}