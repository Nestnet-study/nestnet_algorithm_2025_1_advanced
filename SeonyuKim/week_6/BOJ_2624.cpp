#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T, k;
    cin >> T;
    cin >> k;

    vector<pair<int, int>> coins(k);
    for (int i = 0; i < k; ++i) {
        cin >> coins[i].first >> coins[i].second;
    }

    vector<int> dp(T + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < k; ++i) {
        int coin_value = coins[i].first;  
        int coin_count = coins[i].second; 

        for (int j = T; j >= 1; --j) {

            for (int count = 1; count <= coin_count; ++count) {
                int previous_amount = j - count * coin_value; 

                if (previous_amount < 0) {
                    break; 
                }
                dp[j] += dp[previous_amount];
            }
        }
    }

    cout << dp[T] << endl;

    return 0;
}