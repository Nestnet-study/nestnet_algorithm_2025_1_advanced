#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    deque<int> A(2 * N);
    deque<bool> robot_on_belt(2 * N, false); 
    int zero_durability_count = 0;

    for (int i = 0; i < 2 * N; ++i) {
        cin >> A[i];
    }

    int stage = 0;

    while (true) {
        stage++;

        // 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        A.push_front(A.back());
        A.pop_back();
        robot_on_belt.push_front(robot_on_belt.back());
        robot_on_belt.pop_back();

        // 회전 후, 만약 로봇이 내리는 위치(N-1번 칸)에 도달하면 즉시 내린다.
        if (robot_on_belt[N - 1]) {
            robot_on_belt[N - 1] = false;
        }

        // 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        // (가장 먼저 올라간 로봇 = 내리는 위치에 가장 가까운 로봇 = N-2 인덱스부터 0 인덱스까지)
        for (int i = N - 2; i >= 0; --i) {
            // 현재 i번 칸에 로봇이 있고, 다음 i+1번 칸에 로봇이 없으며, 다음 칸 내구도가 1 이상인 경우
            if (robot_on_belt[i] && !robot_on_belt[i + 1] && A[i + 1] >= 1) {
                robot_on_belt[i] = false;       // 현재 칸에서 로봇 제거
                robot_on_belt[i + 1] = true;    // 다음 칸으로 로봇 이동
                A[i + 1]--;                     // 다음 칸 내구도 감소
                if (A[i + 1] == 0) {
                    zero_durability_count++;
                }
            }
        }
        
        // 로봇 이동 후, 만약 로봇이 내리는 위치(N-1번 칸)에 도달하면 즉시 내린다.
        if (robot_on_belt[N - 1]) {
            robot_on_belt[N - 1] = false;
        }

        // 3. 올리는 위치(0번 칸)에 있는 칸의 내구도가 0이 아니고, 해당 칸에 로봇이 없다면 로봇을 올린다.
        if (!robot_on_belt[0] && A[0] >= 1) {
            robot_on_belt[0] = true; // 0번 칸에 로봇 올림
            A[0]--;                  // 0번 칸 내구도 감소
            if (A[0] == 0) {
                zero_durability_count++;
            }
        }

        // 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
        if (zero_durability_count >= K) {
            break;
        }
    }

    cout << stage << '\n'; 

    return 0;
}