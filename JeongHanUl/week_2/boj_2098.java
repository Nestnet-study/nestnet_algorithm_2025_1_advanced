package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2098 {
    //public class Main {

    static final int INF = 10_000_000;
    static int n;
    static int[][] weight;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        weight = new int[n][n];
        dp = new int[n][1 << n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                weight[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = tsp(0, 1);
        System.out.println(result);
    }

    static int tsp(int current, int visited) {
        // 베이스 컨디션. 모두 방문
        if (visited == (1 << n) - 1) {
            if (weight[current][0] != 0) {
                return weight[current][0];
            } else {
                return INF;
            }
        }

        // dp에 기록된 경우는 생략
        if (dp[current][visited] != 0) {
            return dp[current][visited];
        }

        int min = INF;
        // 다음 방문할 도시 지정
        for (int next = 0; next < n; next++) {
            if ((visited & (1 << next)) != 0 || weight[current][next] == 0) continue;

            int sum = weight[current][next] + tsp(next, visited | (1 << next));

            min = Math.min(min, sum);
        }

        dp[current][visited] = min;
        return min;
    }
}
