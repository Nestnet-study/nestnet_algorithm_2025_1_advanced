#include <iostream>
#include <deque>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    deque<int> belt(2 * N); // 내구도
    deque<bool> robot(N, false); // 로봇 위치 (위쪽 N칸만 사용)

    for (int i = 0; i < 2 * N; i++) {
        cin >> belt[i];
    }

    int step = 0;

    while (true) {
        step++;

        // 1. 벨트와 로봇 회전
        belt.push_front(belt.back());
        belt.pop_back();

        robot.push_front(false);
        robot.pop_back();
        robot[N - 1] = false; // 내리는 위치에 로봇은 내림

        // 2. 로봇 이동 (오래된 로봇부터 순서대로)
        for (int i = N - 2; i >= 0; i--) {
            if (robot[i] && !robot[i + 1] && belt[i + 1] > 0) {
                robot[i] = false;
                robot[i + 1] = true;
                belt[i + 1]--;
            }
        }
        robot[N - 1] = false; // 내리는 위치에 로봇은 항상 내림

        // 3. 로봇 올리기
        if (belt[0] > 0) {
            robot[0] = true;
            belt[0]--;
        }

        // 4. 내구도가 0인 칸 개수 세기
        int zero_cnt = 0;
        for (int i = 0; i < 2 * N; i++) {
            if (belt[i] == 0) zero_cnt++;
        }

        if (zero_cnt >= K) break;
    }

    cout << step << endl;
    return 0;
}