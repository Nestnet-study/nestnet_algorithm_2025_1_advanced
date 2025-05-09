package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1806 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());

        int start = 0, end = 0;
        int sum = arr[0], length = Integer.MAX_VALUE;
        while (start <= end) {
            if (sum < target) {
                end++;
                if (end >= n) break;
                sum += arr[end];
            } else {
                length = Math.min(length, end - start + 1);
                sum -= arr[start];
                start++;
            }
        }

        if (length == Integer.MAX_VALUE) System.out.println(0);
        else System.out.println(length);
    }
}
