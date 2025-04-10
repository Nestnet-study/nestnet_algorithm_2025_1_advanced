package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_16932 {
    //public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int n;
    static int m;
    static int[][] graph;
    static int[][] group;
    static boolean[][] visited;
    static int sum = 0;
    static Map<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        group = new int[n][m];
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int number = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && graph[i][j] == 1) bfs(i, j, number++);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) continue;

                int cnt = 1;
                Set<Integer> set = new HashSet<>();
                for (int k = 0; k < 4; k++) {
                    int nr = i + dr[k];
                    int nc = j + dc[k];

                    if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                    if (graph[nr][nc] == 0) continue;
                    if (set.contains(group[nr][nc])) continue;

                    cnt += map.get(group[nr][nc]);
                    set.add(group[nr][nc]);
                }

                sum = Math.max(sum, cnt);
            }
        }

        System.out.println(sum);
    }

    static void bfs(int row, int col, int number) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});
        visited[row][col] = true;
        group[row][col] = number;
        int cnt = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curRow = current[0];
            int curCol = current[1];
            cnt++;

            for (int i = 0; i < 4; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (graph[nr][nc] == 0) continue;
                if (visited[nr][nc]) continue;

                queue.add(new int[]{nr, nc});
                visited[nr][nc] = true;
                group[nr][nc] = number;
            }
        }

        map.put(number, cnt);
    }
}
