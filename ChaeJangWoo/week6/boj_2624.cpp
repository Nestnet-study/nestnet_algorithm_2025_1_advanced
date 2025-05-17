#include <iostream>
#include <vector>
using namespace std;

struct Coin
{
    int price;
    int num;
};

int main()
{
    int T, k;
    cin >> T >> k;

    vector<Coin> coins(k);
    for (int i = 0; i < k; i++)
    {
        cin >> coins[i].price >> coins[i].num;
    }

    vector<int> dp(T + 1, 0);
    dp[0] = 1; // 0원을 만드는 방법은 아무 동전도 안 쓰는 1가지

    for (int i = 0; i < k; i++)
    {
        int value = coins[i].price;
        int count = coins[i].num;

        // 임시 DP 배열 사용: 현재 동전 적용한 결과 누적
        vector<int> temp(dp);

        for (int money = 0; money <= T; money++)
        {
            if (dp[money] > 0)
            {
                for (int use = 1; use <= count; use++)
                {
                    int next = money + value * use;
                    if (next > T)
                        break;
                    temp[next] += dp[money];
                }
            }
        }

        dp = temp;
    }

    cout << dp[T] << '\n';
    return 0;
}