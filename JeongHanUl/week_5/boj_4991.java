package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj_4991 {
    //public class Main {

    static int h, w;
    static int min;
    static int[][] graph;
    static char[][] map;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0) return;

            int[] start = new int[2];
            List<int[]> list = new ArrayList<>();
            map = new char[h][w];
            for (int i = 0; i < h; i++) {
                String str = br.readLine();
                for (int j = 0; j < w; j++) {
                    char ch = str.charAt(j);
                    if (ch == 'o') {
                        start[0] = i;
                        start[1] = j;
                    }
                    if (ch == '*') list.add(new int[]{i, j});
                    map[i][j] = ch;
                }
            }

            int[][] distance = new int[h][w];
            bfs(start, distance);

            graph = new int[list.size() + 1][list.size() + 1];
            for (int i = 1; i <= list.size(); i++) {
                int[] node = list.get(i - 1);
                int r = node[0];
                int c = node[1];
                graph[0][i] = distance[r][c];
            }

            for (int i = 1; i <= list.size(); i++) {
                int[][] dist = new int[h][w];
                bfs(list.get(i - 1), dist);

                for (int j = 1; j <= list.size(); j++) {
                    if (i == j) continue;

                    int[] node = list.get(j - 1);
                    int r = node[0];
                    int c = node[1];
                    graph[i][j] = dist[r][c];
                }
            }

            min = Integer.MAX_VALUE;
            boolean flag = true;
            for (int i = 1; i <= list.size(); i++) {
                if (graph[0][i] == 0) {
                    flag = false;
                    break;
                }

                boolean[] visited = new boolean[list.size() + 1];
                visited[i] = true;
                dfs(1, i, graph[0][i], visited);
                visited[i] = false;
            }

            if (flag) System.out.println(min);
            else System.out.println(-1);
        }
    }

    static void bfs(int[] start, int[][] distance) {
        boolean[][] visited = new boolean[h][w];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(start);
        visited[start[0]][start[1]] = true;
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curRow = current[0];
            int curCol = current[1];

            for (int i = 0; i < 4; i++) {
                int nr = curRow + dr[i];
                int nc = curCol + dc[i];

                if (nr < 0 || nr >= h || nc < 0 || nc >= w) continue;
                if (visited[nr][nc]) continue;
                if (map[nr][nc] == 'x') continue;

                visited[nr][nc] = true;
                distance[nr][nc] = distance[curRow][curCol] + 1;
                queue.add(new int[]{nr, nc});
            }
        }
    }

    static void dfs(int depth, int current, int sum, boolean[] visited) {
        if (depth == visited.length - 1) {
            min = Math.min(min, sum);
            return;
        }

        for (int i = 1; i < visited.length; i++) {
            if (visited[i] || graph[current][i] == 0) continue;

            visited[i] = true;
            dfs(depth + 1, i, sum + graph[current][i], visited);
            visited[i] = false;
        }
    }
}
