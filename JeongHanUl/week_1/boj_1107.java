package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_1;

import java.io.*;
import java.util.*;

public class boj_1107 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int target = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        Set<Integer> set = new HashSet<>();
        if (m != 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) set.add(Integer.parseInt(st.nextToken()));
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i <= 1_000_000; i++) {
            String numStr = String.valueOf(i);
            boolean flag = true;

            for (int j = 0; j < numStr.length(); j++) {
                char digitChar = numStr.charAt(j);
                int digit = digitChar - '0';
                if (set.contains(digit)) {
                    flag = false;
                    break;
                }
            }

            if (!flag) continue;

            min = Math.min(min, String.valueOf(i).length() + Math.abs(target - i));
        }

        min = Math.min(min, Math.abs(target - 100));

        System.out.println(min);
    }
}
