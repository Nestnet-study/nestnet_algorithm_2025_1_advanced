package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2240 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int[] plum = new int[t];
        for (int i = 0; i < t; i++) {
            plum[i] = Integer.parseInt(br.readLine());
        }

        int[][][] dp = new int[t][2][w + 1];
        if (plum[0] == 1) dp[0][0][w]++;
        else dp[0][1][w - 1]++;

        for (int time = 1; time < t; time++) {
            int current = plum[time];

            // 1번 나무에서 떨어짐
            if (current == 1) {
                for (int i = w; i >= 0; i--) {
                    dp[time][1][i] = dp[time - 1][1][i];
                }

                // 움직이지 않아도 됨
                for (int i = w; i >= 0; i--) {
                    dp[time][0][i] = Math.max(dp[time][0][i], dp[time - 1][0][i] + 1);
                }

                // 움직여야 됨
                for (int i = w - 1; i >= 0; i--) {
                    dp[time][0][i] = Math.max(dp[time][0][i], dp[time - 1][1][i + 1] + 1);
                }
            }
            // 2번 나무에서 떨어짐
            else {
                for (int i = w; i >= 0; i--) {
                    dp[time][0][i] = dp[time - 1][0][i];
                }

                // 움직이지 않아도 됨
                for (int i = w; i >= 0; i--) {
                    dp[time][1][i] = Math.max(dp[time][1][i], dp[time - 1][1][i] + 1);
                }

                // 움직여야 됨
                for (int i = w - 1; i >= 0; i--) {
                    dp[time][1][i] = Math.max(dp[time][1][i], dp[time - 1][0][i + 1] + 1);
                }
            }
        }

        int max = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j <= w; j++) max = Math.max(max, dp[t - 1][i][j]);
        }
        System.out.println(max);
    }
}
