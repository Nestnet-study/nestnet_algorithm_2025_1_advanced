package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_15684 {
    //public class Main {

    static int min = -1;
    static boolean[][] sadari;
    static int n, m, h;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        sadari = new boolean[h + 1][n];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sadari[a][b] = true;
        }

        // 0~3까지 사다리 배치
        for (int i = 0; i <= 3; i++) {
            place(1, 1, 0, i);

            if (min != -1) break;
        }

        System.out.println(min);
    }

    static void place(int r, int c, int level, int depth) {
        if (level == depth) {
            // 통과 가능?
            boolean flag = true;
            for (int i = 1; i < n; i++) {
                if (!simulate(i)) {
                    flag = false;
                    break;
                }
            }

            if (flag) min = depth;
            return;
        }

        // 사다리 배치하기
        for (int j = c; j < n; j++) {
            if (sadari[r][j]) continue;

            if (j - 1 > 0 && sadari[r][j - 1]) continue;
            if (j + 1 < n && sadari[r][j + 1]) continue;

            sadari[r][j] = true;
            place(r, j + 1, level + 1, depth);
            sadari[r][j] = false;
        }
        for (int i = r + 1; i <= h; i++) {
            for (int j = 1; j < n; j++) {
                if (sadari[i][j]) continue;

                if (j - 1 > 0 && sadari[i][j - 1]) continue;
                if (j + 1 < n && sadari[i][j + 1]) continue;

                sadari[i][j] = true;
                place(i, j + 1, level + 1, depth);
                sadari[i][j] = false;
            }
        }
    }
    static boolean simulate(int target) {
        int status = target;

        for (int k = 1; k <= h; k++) {
            if (status - 1 > 0 && sadari[k][status - 1]) {
                status -= 1;
            } else if (status < n && sadari[k][status]) {
                status += 1;
            }
        }
        return status == target;
    }
}
