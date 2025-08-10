package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2616 {
    //public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n + 1];
        int[] prefixSum = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }
        int m = Integer.parseInt(br.readLine());

        int[][] dp = new int[4][n + 1];
        for (int i = 1; i < 4; i++) {
            for (int j = i * m; j <= n; j++) {
                dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j - m] + (prefixSum[j] - prefixSum[j - m]));
            }
        }

        System.out.println(dp[3][n]);
    }
}
