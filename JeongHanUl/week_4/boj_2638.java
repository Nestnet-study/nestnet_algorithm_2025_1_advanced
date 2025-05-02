package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_2638 {
    //public class Main {

    static int n, m;
    static int[][] map;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) map[i][j] = Integer.parseInt(st.nextToken());
        }

        int time = 0;
        boolean flag;
        do {
            time++;
            flag = false;
            int[][] cnt = new int[n][m];
            bfs(cnt);

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (cnt[i][j] < 2) continue;

                    map[i][j] = 0;
                    flag = true;
                }
            }
        } while (flag);

        System.out.println(time - 1);
    }

    static void bfs(int[][] cnt) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curRow = current[0];
            int curCol = current[1];

            for (int i = 0; i < 4; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (visited[nr][nc]) continue;

                if (map[nr][nc] == 1) {
                    cnt[nr][nc]++;
                    continue;
                }

                queue.add(new int[]{nr, nc});
                visited[nr][nc] = true;
            }
        }
    }
}
