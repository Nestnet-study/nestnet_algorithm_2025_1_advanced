#include <bits/stdc++.h> /

using namespace std; 

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; 
    int S; 
    
    cin >> N >> S;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int left = 0; 
    int sum = 0; 
    int min_length = N + 1; 
    
    for (int right = 0; right < N; ++right) {
        sum += A[right]; 
       
        while (sum >= S) {
            min_length = min(min_length, right - left + 1);
            sum -= A[left];
            left++; 
        }

    }

    if (min_length == N + 1) {
        cout << 0 << endl;
    } else {
        cout << min_length << endl;
    }
    return 0;
}