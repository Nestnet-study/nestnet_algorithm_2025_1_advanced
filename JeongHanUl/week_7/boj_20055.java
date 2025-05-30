package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_20055 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] con = new int[2 * n][2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2 * n; i++) {
            con[i][1] = Integer.parseInt(st.nextToken());
        }
        int cnt = 0;
        int output = 0;

        while (cnt < k) {
            output++;

            // 벨트 미루기
            int t1 = con[2 * n - 1][0];
            int t2 = con[2 * n - 1][1];
            for (int i = 2 * n - 1; i > 0; i--) {
                con[i][0] = con[i - 1][0];
                con[i][1] = con[i - 1][1];
            }
            con[0][0] = t1;
            con[0][1] = t2;

            // n-1에서 로봇 내림
            if (con[n - 1][0] == 1) con[n - 1][0] = 0;

            // 로봇 이동. n-1 ~ 1. 내구도 카운트
            for (int i = n - 1; i > 0; i--) {
                if (con[i][1] == 0) continue;
                if (con[i][0] == 1 || con[i - 1][0] == 0) continue;

                con[i][0] = 1;
                con[i - 1][0] = 0;
                if (--con[i][1] == 0) cnt++;
            }

            // n-1에서 로봇 내림
            if (con[n - 1][0] == 1) con[n - 1][0] = 0;

            // 로봇 올림. 내구도 카운트
            if (con[0][1] != 0 && con[0][0] == 0) {
                con[0][0] = 1;

                if (--con[0][1] == 0) cnt++;
            }
        }

        System.out.println(output);
    }
}
