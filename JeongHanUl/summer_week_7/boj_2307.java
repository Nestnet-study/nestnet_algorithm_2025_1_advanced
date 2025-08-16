package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_2307 {
    //public class Main {

    static int n, m;
    static int origin;
    static int time;
    static int max;
    static List<List<int[]>> graph = new ArrayList<>();
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        parent = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph.get(s).add(new int[]{e, w});
            graph.get(e).add(new int[]{s, w});
        }

        // 초기 최단 거리 계산
        origin = dijkstra(0, 0, true);

        // 최소 경로의 엣지 계산
        List<int[]> list = new ArrayList<>();
        int cur = n;
        while (cur != 0 && parent[cur] != 0) {
            list.add(new int[]{parent[cur], cur});
            cur = parent[cur];
        }

        // 엣지 하나씩 제거하고 다익스트라
        for (int[] r : list) {
            int s = r[0];
            int e = r[1];

            time = 0;

            time = dijkstra(s, e, false);

            max = Math.max(max, time - origin);
        }

        System.out.println(max == Integer.MAX_VALUE - origin ? -1 : max);
    }

    static int dijkstra(int s, int e, boolean tracking) {
        int[] distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.add(new int[]{1, distance[1]});
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int curNode = current[0];
            int curWeight = current[1];

            if (curWeight > distance[curNode]) continue;

            for (int[] next : graph.get(curNode)) {
                int nextNode = next[0];
                int nextWeight = next[1];

                if (curNode == s && nextNode == e) continue;
                if (curNode == e && nextNode == s) continue;

                if (nextWeight + distance[curNode] < distance[nextNode]) {
                    distance[nextNode] = nextWeight + distance[curNode];
                    if (tracking) parent[nextNode] = curNode;
                    pq.add(new int[]{nextNode, distance[nextNode]});
                }
            }
        }

        return distance[n];
    }
}
