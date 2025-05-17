package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1749 {
    //public class Main {

    static int[][] matrix;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = Integer.MIN_VALUE;
        for (int start = 0; start < n; start++) {
            int[] temp = new int[m];

            for (int end = start; end < n; end++) {
                for (int col = 0; col < m; col++) temp[col] += matrix[end][col];

                answer = Math.max(answer, kadane(temp));
            }
        }

        System.out.println(answer);
    }

    static int kadane(int[] arr) {
        int current = arr[0];
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            current = Math.max(current + arr[i], arr[i]);
            max = Math.max(max, current);
        }

        return max;
    }
}
