package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1256 {
    //public class Main {

    static final int MAX = 1_000_000_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) dp[i][0] = 1;
        for (int j = 0; j <= m; j++) dp[0][j] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = Math.min(dp[i - 1][j] + dp[i][j - 1], MAX);
            }
        }

        int p = n;
        int q = m;
        if (k > dp[n][m]) System.out.println(-1);
        else {
            StringBuilder sb = new StringBuilder();
            while (k > 0) {
                if (k == dp[p][q]) {
                    sb.append("z".repeat(q)).append("a".repeat(p));
                    break;
                }

                if (k > dp[p - 1][q]) {
                    sb.append("z");
                    k -= dp[p - 1][q];
                    q--;
                } else {
                    sb.append("a");
                    p--;
                }
            }

            System.out.println(sb);
        }
    }
}
