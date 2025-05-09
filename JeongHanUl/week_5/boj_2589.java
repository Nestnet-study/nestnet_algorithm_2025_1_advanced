package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_2589 {
    //public class Main {

    static char[][] map;
    static int n, m;
    static int max = 0;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[n][m];
        for (int i = 0; i < n; i++) map[i] = br.readLine().toCharArray();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'W') continue;

                bfs(i, j);
            }
        }

        System.out.println(max);
//        for (int i = 0; i < n; i++) System.out.println(Arrays.toString(map[i]));
    }

    static void bfs(int row, int col) {
        int[][] dist = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});
        visited[row][col] = true;
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curRow = current[0];
            int curCol = current[1];
            max = Math.max(max, dist[curRow][curCol]);

            for (int i = 0; i < 4; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (visited[nr][nc]) continue;
                if (map[nr][nc] == 'W') continue;

                dist[nr][nc] = dist[curRow][curCol] + 1;
                visited[nr][nc] = true;
                queue.add(new int[]{nr, nc});
            }
        }
    }
}
