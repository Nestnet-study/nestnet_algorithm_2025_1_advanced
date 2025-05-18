#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// 접두어 관계 확인 함수
bool hasInconsistency(vector<string> &phone_list)
{
    sort(phone_list.begin(), phone_list.end()); // 사전순 정렬

    for (int i = 0; i < phone_list.size() - 1; i++)
    {
        string &a = phone_list[i];
        string &b = phone_list[i + 1];

        // a가 b의 접두어인지 확인
        if (b.substr(0, a.size()) == a)
        {
            return true; // 일관성 위반
        }
    }

    return false; // 모두 괜찮음
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<string> phone_list(n);

        for (int i = 0; i < n; i++)
        {
            cin >> phone_list[i];
        }

        if (hasInconsistency(phone_list))
        {
            cout << "NO\n";
        }
        else
        {
            cout << "YES\n";
        }
    }

    return 0;
}