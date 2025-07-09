package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_9328 {
    //public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            char[][] map = new char[n][];
            for (int i = 0; i < n; i++) map[i] = br.readLine().toCharArray();
            boolean[] key = new boolean[26];
            String str = br.readLine();
            if (!str.equals("0")) for (int i = 0; i < str.length(); i++) key[str.charAt(i) - 'a'] = true;
            List<int[]> door = new ArrayList<>();

            // 가장자리 중 들어갈 수 있는 곳 큐에 추가
            Queue<int[]> queue = new LinkedList<>();
            boolean[][] visited = new boolean[n][m];
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (i != 0 && i != n - 1 && j != 0 && j != m - 1) continue;

                    if (map[i][j] == '*') continue;

                    if (map[i][j] >= 'A' && map[i][j] <= 'Z') {
                        door.add(new int[]{map[i][j] - 'A', i, j});
                        continue;
                    }

                    queue.add(new int[]{i, j});
                    visited[i][j] = true;
                    if (map[i][j] == '$') cnt++;
                    else if (map[i][j] >= 'a' && map[i][j] <= 'z') key[map[i][j] - 'a'] = true;
                }
            }

            boolean flag = true;
            while (flag) {
                flag = false;

                // bfs
                while (!queue.isEmpty()) {
                    int[] current = queue.poll();
                    int curRow = current[0];
                    int curCol = current[1];

                    for (int i = 0; i < 4; i++) {
                        int nr = curRow + dr[i];
                        int nc = curCol + dc[i];

                        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                        if (visited[nr][nc]) continue;
                        if (map[nr][nc] == '*') continue;

                        if (map[nr][nc] >= 'A' && map[nr][nc] <= 'Z') {
                            door.add(new int[]{map[nr][nc] - 'A', nr, nc});
                            continue;
                        }

                        queue.add(new int[]{nr, nc});
                        visited[nr][nc] = true;
                        if (map[nr][nc] == '$') cnt++;
                        else if (map[nr][nc] >= 'a' && map[nr][nc] <= 'z') key[map[nr][nc] - 'a'] = true;
                    }
                }

                for (int i = 0; i < door.size(); i++) {
                    if (!key[door.get(i)[0]]) continue;

                    queue.add(new int[]{door.get(i)[1], door.get(i)[2]});
                    visited[door.get(i)[1]][door.get(i)[2]] = true;

                    door.remove(i);
                    flag = true;
                    i--;
                }
            }

            sb.append(cnt).append("\n");
        }

        System.out.println(sb);
    }
}
