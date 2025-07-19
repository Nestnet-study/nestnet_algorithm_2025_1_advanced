package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2169 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] map = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) map[i][j] = Integer.parseInt(st.nextToken());
        }
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i <= m; i++) dp[1][i] += dp[1][i - 1] + map[1][i];

        for (int i = 2; i <= n; i++) {
            // 오른쪽
            int[] right = new int[m + 1];
            right[1] = dp[i - 1][1] + map[i][1];
            for (int j = 2; j <= m; j++) {
                right[j] = Math.max(dp[i - 1][j] + map[i][j], right[j - 1] + map[i][j]);
            }

            // 왼쪽
            int[] left = new int[m + 1];
            left[m] = dp[i - 1][m] + map[i][m];
            for (int j = m - 1; j >= 1; j--) {
                left[j] = Math.max(dp[i - 1][j] + map[i][j], left[j + 1] + map[i][j]);
            }

            for (int j = 1; j <= m; j++) dp[i][j] = Math.max(right[j], left[j]);
        }

        System.out.println(dp[n][m]);
    }
}
