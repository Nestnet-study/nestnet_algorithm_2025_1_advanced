package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class boj_14226 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int s = Integer.parseInt(br.readLine());
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[2000][2000];
        visited[0][1] = true;
        queue.add(new int[]{1, 0, 0});
        int answer = 0;
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int now = current[0];
            int board = current[1];
            int cnt = current[2];

            if (now == s) {
                answer = cnt;
                break;
            }

            // 복사
            queue.add(new int[]{now, now, cnt + 1});

            // 붙이기
            if (board != 0 && now + board < 2000 && !visited[board][now + board]) {
                queue.add(new int[]{now + board, board, cnt + 1});
                visited[board][now + board] = true;
            }

            // 삭제
            if (now > 1 && !visited[board][now - 1]) {
                queue.add(new int[]{now - 1, board, cnt + 1});
                visited[board][now - 1] = true;
            }
        }

        System.out.println(answer);
    }
}
