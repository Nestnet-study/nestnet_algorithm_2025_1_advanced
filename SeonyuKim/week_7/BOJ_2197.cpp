#include <bits/stdc++.h> 

using namespace std;

int get_lcp(const string& s1, const string& s2) {
    int len = 0;
    int limit = min(s1.length(), s2.length());
    for (int i = 0; i < limit; ++i) {
        if (s1[i] == s2[i]) {
            len++;
        } else {
            break;
        }
    }
    return len;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; ++i) {
        cin >> words[i];
    }

    int max_lcp_len = -1; // LCP가 0일 수도 있으므로, 아예 답을 못 찾은 상태로 시작
    int s_final_idx = -1; 
    int t_final_idx = -1;

    for (int i = 0; i < n; ++i) { // S가 될 단어의 인덱스
        for (int j = 0; j < n; ++j) { // T가 될 단어의 인덱스
            if (i == j) continue; // S와 T는 다른 단어

            int current_lcp = get_lcp(words[i], words[j]);

            bool update = false;
            if (current_lcp > max_lcp_len) {
                update = true;
            } else if (current_lcp == max_lcp_len) {
                // LCP 길이가 같다면, 우선순위에 따라 갱신할지 결정
                // 1. S의 인덱스 (i)가 더 작은 것을 우선
                if (i < s_final_idx) {
                    update = true;
                } 
                // 2. S의 인덱스가 같고, T의 인덱스 (j)가 더 작은 것을 우선
                else if (i == s_final_idx) {
                    if (j < t_final_idx) {
                        update = true;
                    }
                }
            }

            if (update) {
                max_lcp_len = current_lcp;
                s_final_idx = i;
                t_final_idx = j;
            }
        }
    }

    cout << words[s_final_idx] << "\n";
    cout << words[t_final_idx] << "\n";

    return 0;
}