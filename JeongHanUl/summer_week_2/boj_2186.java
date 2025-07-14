package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2186 {
    //public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) map[i] = br.readLine().toCharArray();
        String target = br.readLine();

        int[][][] dp = new int[target.length()][n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                if (map[i][j] == target.charAt(target.length() - 1)) dp[target.length() - 1][i][j]++;
        }

        for (int level = target.length() - 2; level >= 0; level--) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (map[i][j] != target.charAt(level)) continue;

                    for (int p = 1; p <= k; p++) {
                        for (int q = 0; q < 4; q++) {
                            int nr = i + p * dr[q];
                            int nc = j + p * dc[q];

                            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;

                            dp[level][i][j] += dp[level + 1][nr][nc];
                        }
                    }
                }
            }
        }


        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                if (dp[0][i][j] != 0) answer += dp[0][i][j];
        }
        System.out.println(answer);
    }
}
