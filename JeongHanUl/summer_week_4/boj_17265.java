package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class boj_17265 {
    //public class Main {

    static int[] dr = {1, 0};
    static int[] dc = {0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] map = new char[n][n];
        for (int i = 0; i < n; i++) {
            String str = br.readLine().replace(" ", "");

            for (int j = 0; j < n; j++) map[i][j] = str.charAt(j);
        }

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, map[0][0] - '0', 0});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curRow = current[0];
            int curCol = current[1];
            int curResult = current[2];
            int op = current[3];

            if (curRow == n - 1 && curCol == n - 1) {
                max = Math.max(max, curResult);
                min = Math.min(min, curResult);
                continue;
            }

            for (int i = 0; i < 2; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0|| nr >= n || nc < 0 || nc >= n) continue;

                if (op == 1) {
                    queue.add(new int[]{nr, nc, curResult + (map[nr][nc] - '0'), 0});
                } else if (op == 2) {
                    queue.add(new int[]{nr, nc, curResult - (map[nr][nc] - '0'), 0});
                } else if (op == 3) {
                    queue.add(new int[]{nr, nc, curResult * (map[nr][nc] - '0'), 0});
                } else {
                    if (map[nr][nc] == '+') queue.add(new int[]{nr, nc, curResult, 1});
                    else if (map[nr][nc] == '-') queue.add(new int[]{nr, nc, curResult, 2});
                    else if (map[nr][nc] == '*') queue.add(new int[]{nr, nc, curResult, 3});
                }
            }
        }

        System.out.println(max + " " + min);
    }
}
