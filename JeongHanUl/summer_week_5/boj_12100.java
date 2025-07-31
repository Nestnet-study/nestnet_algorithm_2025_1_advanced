package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_12100 {
    //public class Main {

    static int n;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                max = Math.max(max, map[i][j]);
            }
        }

        dfs(map, 0);

        System.out.println(max);
    }

    static void dfs(int[][] map, int level) {
        if (level == 5) return;

        for (int i = 0; i < n; i++) System.out.println(Arrays.toString(map[i]));
        System.out.println();

        for (int i = 0; i < 4; i++) {
            int[][] next = new int[n][];
            for (int j = 0; j < n; j++) next[j] = Arrays.copyOf(map[j], n);

            move(next, i);
            dfs(next, level + 1);
        }
    }
    static void move(int[][] map, int d) {
        boolean[][] join = new boolean[n][n];

        if (d == 0) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (map[i][j] == 0) continue;

                    int nr = i + dr[d];
                    int nc = j + dc[d];

                    while (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && map[nr][nc] == 0) {
                        nr += dr[d];
                        nc += dc[d];
                    }

                    int temp = map[nr - dr[d]][nc - dc[d]];
                    map[nr - dr[d]][nc - dc[d]] = map[i][j];
                    map[i][j] = temp;

                    if (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && !join[nr][nc] && map[nr][nc] == map[nr - dr[d]][nc - dc[d]]) {
//                        System.out.println("------");
//                        for (int k = 0; k < n; k++) System.out.println(Arrays.toString(map[k]));

                        map[nr][nc] *= 2;
                        map[nr - dr[d]][nc - dc[d]] = 0;
                        join[nr][nc] = true;

                        max = Math.max(max, map[nr][nc]);
                    }
                }
            }
        } else if (d == 1) {
            for (int i = n - 1; i >= 0; i--) {
                for (int j = 0; j < n; j++) {
                    if (map[i][j] == 0) continue;

                    int nr = i + dr[d];
                    int nc = j + dc[d];

                    while (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && map[nr][nc] == 0) {
                        nr += dr[d];
                        nc += dc[d];
                    }

                    int temp = map[nr - dr[d]][nc - dc[d]];
                    map[nr - dr[d]][nc - dc[d]] = map[i][j];
                    map[i][j] = temp;


                    if (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && !join[nr][nc] && map[nr][nc] == map[nr - dr[d]][nc - dc[d]]) {
                        map[nr][nc] *= 2;
                        map[nr - dr[d]][nc - dc[d]] = 0;
                        join[nr][nc] = true;

                        max = Math.max(max, map[nr][nc]);
                    }
                }
            }
        } else if (d == 2) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (map[i][j] == 0) continue;

                    int nr = i + dr[d];
                    int nc = j + dc[d];

                    while (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && map[nr][nc] == 0) {
                        nr += dr[d];
                        nc += dc[d];
                    }

                    int temp = map[nr - dr[d]][nc - dc[d]];
                    map[nr - dr[d]][nc - dc[d]] = map[i][j];
                    map[i][j] = temp;

                    if (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && !join[nr][nc] && map[nr][nc] == map[nr - dr[d]][nc - dc[d]]) {
                        map[nr][nc] *= 2;
                        map[nr - dr[d]][nc - dc[d]] = 0;
                        join[nr][nc] = true;

                        max = Math.max(max, map[nr][nc]);
                    }
                }
            }
        } else if (d == 3) {
            for (int i = 0; i < n; i++) {
                for (int j = n - 1; j >= 0; j--) {
                    if (map[i][j] == 0) continue;

                    int nr = i + dr[d];
                    int nc = j + dc[d];

                    while (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && map[nr][nc] == 0) {
                        nr += dr[d];
                        nc += dc[d];
                    }

                    int temp = map[nr - dr[d]][nc - dc[d]];
                    map[nr - dr[d]][nc - dc[d]] = map[i][j];
                    map[i][j] = temp;


                    if (!(nr < 0 || nr >= n || nc < 0 || nc >= n) && !join[nr][nc] && map[nr][nc] == map[nr - dr[d]][nc - dc[d]]) {
                        map[nr][nc] *= 2;
                        map[nr - dr[d]][nc - dc[d]] = 0;
                        join[nr][nc] = true;

                        max = Math.max(max, map[nr][nc]);
                    }
                }
            }
        }
    }
}
