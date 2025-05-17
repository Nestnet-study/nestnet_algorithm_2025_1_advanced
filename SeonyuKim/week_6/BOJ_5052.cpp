#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        vector<string> phone_numbers(n);
        for(int i = 0; i < n; ++i){
            cin >> phone_numbers[i];
        }
        sort(phone_numbers.begin(), phone_numbers.end());
        bool is_consistent = true;
        for(int i = 1; i < n; ++i){
            if(phone_numbers[i].find(phone_numbers[i-1]) == 0){
                is_consistent = false;
                break;
            }
        }
        cout << (is_consistent ? "YES" : "NO") << "\n";
}
}