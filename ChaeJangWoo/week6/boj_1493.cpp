#include <iostream>
#include <algorithm>
using namespace std;

int length, width, height, n;
int cube[20]; // cube[i]는 2^i 크기의 큐브 개수

int main()
{

    cin >> length >> width >> height;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        cube[a] = b;
    }

    long long total_volume = 1LL * length * width * height;
    long long filled = 0;
    long long used = 0;

    for (int i = 19; i >= 0; i--)
    {
        int size = 1 << i;
        long long max_count = (long long)(length / size) * (width / size) * (height / size);

        // max_count는 현재 크기의 큐브로 넣을 수 있는 위치 수
        max_count -= filled / (1LL << (3 * i)); // 이미 채운 부피만큼 위치 수 차감

        long long use = min((long long)cube[i], max_count);

        filled += use * (1LL << (3 * i)); // 부피 단위로 누적
        used += use;
    }

    if (filled == total_volume)
        cout << used << '\n';
    else
        cout << -1 << '\n';

    return 0;
}