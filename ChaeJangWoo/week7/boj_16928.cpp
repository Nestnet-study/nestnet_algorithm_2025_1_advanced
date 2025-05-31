#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int board[101];     // 각 칸에 도착했을 때 이동할 위치 저장 (사다리/뱀 반영)
int visited[101];   // 방문 여부 및 이동 횟수 저장

int main() {
    int N, M;
    cin >> N >> M;

    // 초기화: board[i] = i (자기 자신으로 이동)
    for (int i = 1; i <= 100; i++) {
        board[i] = i;
    }

    // 사다리 입력
    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        board[x] = y;
    }

    // 뱀 입력
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        board[u] = v;
    }

    queue<int> q;
    q.push(1);
    visited[1] = 0;

    while (!q.empty()) {
        int curr = q.front();
        q.pop();

        for (int dice = 1; dice <= 6; dice++) {
            int next = curr + dice;
            if (next > 100) continue;

            next = board[next]; // 사다리 또는 뱀 타고 이동한 위치

            if (visited[next] == 0 && next != 1) {
                visited[next] = visited[curr] + 1;
                q.push(next);
            }

            if (next == 100) {
                cout << visited[100] << '\n';
                return 0;
            }
        }
    }

    return 0;
}