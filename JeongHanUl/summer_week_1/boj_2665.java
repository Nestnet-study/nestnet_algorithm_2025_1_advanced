package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class boj_2665 {
    //public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);
        String[] map = new String[n];
        for (int i = 0; i < n; i++) map[i] = br.readLine();

        dist[0][0] = 0;
        Deque<int[]> deque = new LinkedList<>();
        deque.add(new int[]{0, 0, 0});
        while (!deque.isEmpty()) {
            int[] current = deque.poll();
            int curRow = current[0];
            int curCol = current[1];
            int curCnt = current[2];
            for (int i = 0; i < 4; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;

                int nextCnt = curCnt;
                if (map[nr].charAt(nc) == '0') nextCnt++;

                if (dist[nr][nc] <= nextCnt) continue;

                dist[nr][nc] = nextCnt;
                if (map[nr].charAt(nc) == '1') deque.addFirst(new int[]{nr, nc, nextCnt});
                else deque.addLast(new int[]{nr, nc, nextCnt});
            }
        }

        System.out.println(dist[n - 1][n - 1]);
    }
}
