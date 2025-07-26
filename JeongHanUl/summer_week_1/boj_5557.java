package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_5557 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[][] dp = new long[n][21];
        String[] num = br.readLine().split(" ");

        dp[1][Integer.parseInt(num[0])] = 1;
        for (int i = 2; i < n; i++) {
            int k = Integer.parseInt(num[i - 1]);

            for (int j = 0; j <= 20; j++) {
                if (j - k >= 0) {
                    dp[i][j] += dp[i - 1][j - k];
                }

                if (j + k <= 20) {
                    dp[i][j] += dp[i - 1][j + k];
                }
            }
        }

        System.out.println(dp[n - 1][Integer.parseInt(num[n - 1])]);
    }
}
