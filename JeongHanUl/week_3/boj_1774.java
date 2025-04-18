package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_1774 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<long[]> input = new ArrayList<>();
        input.add(new long[]{});
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            input.add(new long[]{Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())});
        }

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                double w = Math.sqrt(
                        Math.pow(input.get(i)[0] - input.get(j)[0], 2) + Math.pow(input.get(i)[1] - input.get(j)[1], 2));
                graph.get(i).add(new Node(j, w));
                graph.get(j).add(new Node(i, w));
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            graph.get(s).add(new Node(e, 0));
            graph.get(e).add(new Node(s, 0));
        }
        boolean[] visited = new boolean[n + 1];
        int cnt = 0;
        double total = 0;

        Queue<Node> pq = new PriorityQueue<>(Comparator.comparing(a -> a.weight));
        pq.add(new Node(1, 0));
        while (!pq.isEmpty() && cnt < n) {
            Node current = pq.poll();
            int curDestination = current.destination;
            double curWeight = current.weight;

            if (visited[curDestination]) continue;

            for (Node node : graph.get(curDestination)) pq.add(node);
            visited[curDestination] = true;
            total += curWeight;
            cnt++;
        }

        System.out.printf("%.2f\n", total);
    }

    static class Node {
        public int destination;
        public double weight;

        Node(int d, double w) {
            this.destination = d;
            this.weight = w;
        }
    }
}
