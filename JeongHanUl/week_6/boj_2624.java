package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2624 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int target = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] coins = new int[k];
        int[] cnt = new int[k];

        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            coins[i] = Integer.parseInt(st.nextToken());
            cnt[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[k + 1][target + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= k; i++) {
            int coin = coins[i - 1];
            int count = cnt[i - 1];

            for (int j = 0; j <= target; j++) {
                for (int c = 0; c <= count; c++) {
                    if (j - coin * c < 0) continue;

                    dp[i][j] += dp[i - 1][j - coin * c];
                }
            }
        }

        System.out.println(dp[k][target]);
    }
}
