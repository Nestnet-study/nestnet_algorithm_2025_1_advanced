package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_2342 {
    //public class Main {

    static int[][] cost = {
            {0, 2, 2, 2, 2},
            {0, 1, 3, 4, 3},
            {0, 3, 1, 3, 4},
            {0, 4, 3, 1, 3},
            {0, 3, 4, 3, 1}};
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = st.countTokens() - 1;
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[][][] dp = new int[n + 1][5][5];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < 5; j++) {
                Arrays.fill(dp[i][j], 1_000_000);
            }
        }

        dp[0][0][0] = 0;
        dp[1][arr[0]][0] = cost[0][arr[0]];
        dp[1][0][arr[0]] = cost[0][arr[0]];
        for (int level = 2; level <= n; level++) {
            int current = arr[level - 1];

            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if(dp[level - 1][i][j] == 1_000_000) continue;
                    if(i == j) continue;

                    dp[level][i][current] = Math.min(dp[level][i][current], dp[level - 1][i][j] + cost[j][current]);
                    dp[level][current][j] = Math.min(dp[level][current][j], dp[level - 1][i][j] + cost[i][current]);
//
//                    System.out.println(i + " " + current + " : " + dp[level][i][current]);
//                    System.out.println(current + " " + j + " : " + dp[level][current][j]);
                }
            }
        }

        int answer = 1_000_000;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                answer = Math.min(answer, dp[n][i][j]);
            }
        }
        System.out.println(answer);
    }
}
