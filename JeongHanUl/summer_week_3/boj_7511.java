package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_7511 {
    //public class Main {

    static int[] parent;
    static int[] rank;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int cnt = 0;
        while (++cnt <= t) {
            StringBuilder sb = new StringBuilder();
            sb.append("Scenario ").append(cnt).append(":\n");

            int n = Integer.parseInt(br.readLine());
            int k = Integer.parseInt(br.readLine());
            parent = new int[n];
            for (int i = 0; i< n; i++) parent[i] = i;
            rank = new int[n];

            for (int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());

                union(s, e);
            }

            int m = Integer.parseInt(br.readLine());
            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());

                if (find(s) == find(e)) sb.append(1).append("\n");
                else sb.append(0).append("\n");
            }

            System.out.println(sb);
        }
    }

    public static int find(int a) {
        if (parent[a] == a) return a;

        return parent[a] = find(parent[a]);
    }
    public static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            if (rank[rootA] < rank[rootB]) {
                parent[rootA] = rootB;
            } else if (rank[rootA] > rank[rootB]) {
                parent[rootB] = rootA;
            } else {
                parent[rootA] = rootB;
                rank[rootB]++;
            }
        }
    }
}
