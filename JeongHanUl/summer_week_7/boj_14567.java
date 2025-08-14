package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_14567 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            graph.get(s).add(e);
            indegree[e]++;
        }

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i <= n; i++) {
            if (indegree[i] == 0) queue.add(new int[]{i, 1});
        }
        int[] arr = new int[n + 1];
        Arrays.fill(arr, 1001);
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curNode = current[0];
            int curCnt = current[1];

            arr[curNode] = curCnt;

            for (int k : graph.get(curNode)) {
                indegree[k]--;

                if (indegree[k] == 0) queue.add(new int[]{k, curCnt + 1});
            }
        }

        for (int i = 1; i <= n; i++) System.out.print(arr[i]+ " ");
    }
}
