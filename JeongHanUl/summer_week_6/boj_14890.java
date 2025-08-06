package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_14890 {
    //public class Main {

    static int n, l;
    static int[][] map1;
    static int[][] map2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        map1 = new int[n][n];
        map2 = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int m = Integer.parseInt(st.nextToken());
                map1[i][j] = m;
                map2[j][i] = m;
            }
        }

        int cnt = 0;

        // 행 판단
        for (int i = 0; i < n; i++) {
            boolean flag = true;
            boolean[] arr = new boolean[n];

            for (int j = 1; j < n; j++) {
                if (map1[i][j - 1] == map1[i][j]) continue;

                if (map1[i][j - 1] + 1 == map1[i][j] && isAble(1, i, j - l, j, arr, map1[i][j - 1])) {
                    for (int k = j - l; k < j; k++) arr[k] = true;
                } else if (map1[i][j - 1] - 1 == map1[i][j] && isAble(1, i, j, j + l, arr, map1[i][j])) {
                    for (int k = j; k < j + l; k++) arr[k] = true;
                    j += (l - 1);
                } else {
                    flag = false;
                    break;
                }
            }

            if (flag) cnt++;

        }

        // 열 판단
        for (int i = 0; i < n; i++) {
            boolean flag = true;
            boolean[] arr = new boolean[n];

            for (int j = 1; j < n; j++) {
                if (map2[i][j - 1] == map2[i][j]) continue;

                if (map2[i][j - 1] + 1 == map2[i][j] && isAble(2, i, j - l, j, arr, map2[i][j - 1])) {
                    for (int k = j - l; k < j; k++) arr[k] = true;
                } else if (map2[i][j - 1] - 1 == map2[i][j] && isAble(2, i, j, j + l, arr, map2[i][j])) {
                    for (int k = j; k < j + l; k++) arr[k] = true;
                    j += (l - 1);
                } else {
                    flag = false;
                    break;
                }
            }

            if (flag) cnt++;
        }

        System.out.println(cnt);
    }

    static boolean isAble(int mapNum, int i, int s, int e, boolean[] arr, int target) {
        for (int j = s; j < e; j++) {
            if (j < 0 || e > n || arr[j]) return false;

            if (mapNum == 1 && map1[i][j] != target) return false;
            else if (mapNum == 2 && map2[i][j] != target) return false;
        }

        return true;
    }
}
