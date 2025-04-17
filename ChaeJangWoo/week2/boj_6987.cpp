#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int arr[6][3], goal[6][3], ans[4];
vector<pair<int, int>> v;
bool res = true;

void backTracking(int depth) {
    if (depth == v.size()) {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                if (arr[i][j] != goal[i][j]) return;
            }
        }
    }
    if (depth == v.size()) {
        res = false;
        return;
    }
    int a = v[depth].first, b = v[depth].second;
    // a 승
    arr[a][0]++;
    arr[b][2]++;
    backTracking(depth + 1);
    arr[a][0]--;
    arr[b][2]--;
    // 무승부
    arr[a][1]++;
    arr[b][1]++;
    backTracking(depth + 1);
    arr[a][1]--;
    arr[b][1]--;
    // b 승
    arr[a][2]++;
    arr[b][0]++;
    backTracking(depth + 1);
    arr[a][2]--;
    arr[b][0]--;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int cnt = 0;
    for (int i = 0; i < 6; i++) { // 1
        for (int j = i + 1; j < 6; j++) v.push_back({ i,j });
    }
    while (true) {
        res = true; // 2
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = 0;
                cin >> goal[i][j];
            }
        }
        backTracking(0); // 3
        if (!res) ans[cnt] = 1; // 4
        else ans[cnt] = 0;
        cnt++;
        if (cnt == 4) break;
    }
    for (int i = 0; i < 4; i++) cout << ans[i] << " ";
    return 0;
}