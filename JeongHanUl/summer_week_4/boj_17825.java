package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_17825 {
    //public class Main {

    static int[][] map = {
            {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40},
            {0, 13, 16, 19, 25, 30, 35, 40},
            {0, 22, 24, 25, 30, 35, 40},
            {0, 28, 27, 26, 25, 30, 35, 40}};
    static boolean[][] is = new boolean[4][21];
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] rolls = new int[10];
        for (int i = 0; i < 10; i++) rolls[i] = Integer.parseInt(s[i]);

        // rolls, 지금 점수, index, start
        dfs(rolls, 0, 0, 4);

        System.out.println(max);
    }

    static void dfs(int[] rolls, int index, int score, int start) {
//        System.out.println("score " + score);
//        System.out.println(Arrays.toString(is[0]));
//        System.out.println(Arrays.toString(is[1]));
//        System.out.println(Arrays.toString(is[2]));
//        System.out.println(Arrays.toString(is[3]) + "\n");


        // base condition
        if (index >= 10) {
            max = Math.max(max, score);
            return;
        }

        // 출발 움직이기
        if (start > 0 && !is[0][rolls[index]]) {
            is[0][rolls[index]] = true;
            dfs(rolls, index + 1, score + map[0][rolls[index]], start - 1);
            is[0][rolls[index]] = false;
        }

        // 필드 움직이기
        for (int i = 0; i < 4; i++) {
            // 0
            if (i == 0) {
                for (int j = 1; j <= 20; j++) {
                    if (!is[i][j] || j == 5 || j == 10 || j == 15) continue;

                    int next = j + rolls[index];

                    if (next > 20) {
                        is[i][j] = false;
                        dfs(rolls, index + 1, score, start);
                        is[i][j] = true;
                    }

                    if ((next < 20 && !is[i][next]) ||
                            (next == 20 && !is[1][7] && !is[2][6] && !is[3][7])) {
                        is[i][j] = false;
                        is[i][next] = true;
                        dfs(rolls, index + 1, score + map[i][next], start);
                        is[i][next] = false;
                        is[i][j] = true;
                    }
                }
            }

            // 1
            if (i == 1) {
                if (is[0][5] &&
                        ((rolls[index] < 4 && !is[i][rolls[index]]) ||
                                (rolls[index] >= 4 && !is[1][rolls[index]] && !is[2][rolls[index] - 1] && !is[3][rolls[index]]))) {
                    is[0][5] = false;
                    is[i][rolls[index]] = true;
                    dfs(rolls, index + 1, score + map[i][rolls[index]], start);
                    is[i][rolls[index]] = false;
                    is[0][5] = true;
                }

                for (int j = 1; j <= 7; j++) {
                    if (!is[i][j]) continue;

                    int next = j + rolls[index];

                    if (next > 7) {
                        is[i][j] = false;
                        dfs(rolls, index + 1, score, start);
                        is[i][j] = true;
                    }

                    if ((next < 4 && !is[i][next]) ||
                            (next >= 4 && next < 7 && !is[1][next] && !is[2][next - 1] && !is[3][next]) ||
                            (next == 7 && !is[0][20] && !is[1][7] && !is[2][6] && !is[3][7])) {
                        is[i][j] = false;
                        is[i][next] = true;
                        dfs(rolls, index + 1, score + map[i][next], start);
                        is[i][next] = false;
                        is[i][j] = true;
                    }
                }
            }

            // 2
            if (i == 2) {
                if (is[0][10] &&
                        ((rolls[index] < 3 && !is[i][rolls[index]]) ||
                                (rolls[index] >= 3 && !is[1][rolls[index] + 1] && !is[2][rolls[index]] && !is[3][rolls[index] + 1]))) {
                    is[0][10] = false;
                    is[i][rolls[index]] = true;
                    dfs(rolls, index + 1, score + map[i][rolls[index]], start);
                    is[i][rolls[index]] = false;
                    is[0][10] = true;
                }

                for (int j = 1; j <= 6; j++) {
                    if (!is[i][j]) continue;

                    int next = j + rolls[index];

                    if (next > 6) {
                        is[i][j] = false;
                        dfs(rolls, index + 1, score, start);
                        is[i][j] = true;
                    }

                    if ((next < 3 && !is[i][next]) ||
                            (next >= 3 && next < 6 && !is[1][next + 1] && !is[2][next] && !is[3][next + 1])||
                            (next == 6 && !is[0][20] && !is[1][7] && !is[2][6] && !is[3][7])) {
                        is[i][j] = false;
                        is[i][next] = true;
                        dfs(rolls, index + 1, score + map[i][next], start);
                        is[i][next] = false;
                        is[i][j] = true;
                    }
                }
            }

            // 3
            if (i == 3) {
                if (is[0][15] &&
                        ((rolls[index] < 4 && !is[i][rolls[index]]) ||
                                (rolls[index] >= 4 && !is[1][rolls[index]] && !is[2][rolls[index] - 1] && !is[3][rolls[index]]))) {
                    is[0][15] = false;
                    is[i][rolls[index]] = true;
                    dfs(rolls, index + 1, score + map[i][rolls[index]], start);
                    is[i][rolls[index]] = false;
                    is[0][15] = true;
                }

                for (int j = 1; j <= 7; j++) {
                    if (!is[i][j]) continue;

                    int next = j + rolls[index];

                    if (next > 7) {
                        is[i][j] = false;
                        dfs(rolls, index + 1, score, start);
                        is[i][j] = true;
                    }

                    if ((next < 4 && !is[i][next]) ||
                            (next >= 4 && next <= 7 && !is[1][next] && !is[2][next - 1] && !is[3][next])||
                            (next == 7 && !is[0][20] && !is[1][7] && !is[2][6] && !is[3][7])) {
                        is[i][j] = false;
                        is[i][next] = true;
                        dfs(rolls, index + 1, score + map[i][next], start);
                        is[i][next] = false;
                        is[i][j] = true;
                    }
                }
            }
        }
    }
}
