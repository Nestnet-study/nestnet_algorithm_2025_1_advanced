package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_16928 {
    //public class Main {

    static int[] rolls = {1, 2, 3, 4, 5, 6};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Map<Integer, Integer> shortcut = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            shortcut.put(s, e);
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            shortcut.put(s, e);
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{1, 0});
        Set<Integer> set = new HashSet<>();
        set.add(1);
        int answer = 0;
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cur = current[0];
            int cnt = current[1];

            if (cur == 100) answer = cnt;

            for (int roll : rolls) {
                if (set.contains(cur + roll)) continue;
                if (cur + roll > 100) continue;

                set.add(cur + roll);
                if (shortcut.getOrDefault(cur + roll, -1) != -1) {
                    int val = shortcut.get(cur + roll);
                    set.add(val);
                    queue.add(new int[]{val, cnt + 1});
                    continue;
                }
                queue.add(new int[]{cur + roll, cnt + 1});
            }
        }

        System.out.println(answer);
    }
}
