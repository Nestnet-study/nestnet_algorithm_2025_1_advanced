#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

int N, M;
char map[51][51];
bool visited[51][51];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int bfs(int startY, int startX)
{
    memset(visited, false, sizeof(visited));
    queue<pair<pair<int, int>, int>> q; // ((y, x), 거리)
    q.push({{startY, startX}, 0});
    visited[startY][startX] = true;

    int maxDist = 0;

    while (!q.empty())
    {
        int y = q.front().first.first;
        int x = q.front().first.second;
        int dist = q.front().second;
        q.pop();

        maxDist = max(maxDist, dist);

        for (int i = 0; i < 4; ++i)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny >= 0 && ny < N && nx >= 0 && nx < M)
            {
                if (!visited[ny][nx] && map[ny][nx] == 'L')
                {
                    visited[ny][nx] = true;
                    q.push({{ny, nx}, dist + 1});
                }
            }
        }
    }

    return maxDist;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 0; i < N; ++i)
    {
        cin >> map[i];
    }

    int answer = 0;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (map[i][j] == 'L')
            {
                answer = max(answer, bfs(i, j));
            }
        }
    }

    cout << answer << '\n';
    return 0;
}
