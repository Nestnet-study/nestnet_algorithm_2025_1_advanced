package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_12869 {
    //public class Main {

    static int[][] damage = {
            {9, 3, 1},
            {9, 1, 3},
            {3, 9, 1},
            {3, 1, 9},
            {1, 9, 3},
            {1, 3, 9}};
    static int[][][] dp = new int[61][61][61];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] scv = new int[3];
        for (int i = 0; i < n; i++) scv[i] = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= 60; i++) {
            for (int j = 0; j <= 60; j++) Arrays.fill(dp[i][j], Integer.MAX_VALUE);
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{scv[0], scv[1], scv[2], 0});
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cur1 = current[0];
            int cur2 = current[1];
            int cur3 = current[2];
            int curCnt = current[3];

            for (int i = 0; i < 6; i++) {
                int n1 = Math.max(cur1 - damage[i][0], 0);
                int n2 = Math.max(cur2 - damage[i][1], 0);
                int n3 = Math.max(cur3 - damage[i][2], 0);



                if (dp[n1][n2][n3] <= curCnt + 1) continue;

                dp[n1][n2][n3] = curCnt + 1;
                queue.add(new int[]{n1, n2, n3, curCnt + 1});
            }
        }

        System.out.println(dp[0][0][0]);
    }

}
