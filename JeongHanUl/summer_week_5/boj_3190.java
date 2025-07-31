package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_3190 {
    //public class Main {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[][] apple = new boolean[n + 1][n + 1];
        int[][][] snake = new int[n + 1][n + 1][2];

        // 시작 뱀 세팅
        int[] head = {1, 1};
        int[] tail = {1, 1};
        snake[head[0]][head[1]][0] = 1;
        snake[head[0]][head[1]][1] = 3;

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            String[] s = br.readLine().split(" ");

            apple[Integer.parseInt(s[0])][Integer.parseInt(s[1])] = true;
        }
        int l = Integer.parseInt(br.readLine());
        Direction[] dir = new Direction[l];
        for (int i = 0; i < l; i++) {
            String[] s = br.readLine().split(" ");

            dir[i] = new Direction(Integer.parseInt(s[0]), s[1].charAt(0));
        }

        int time = 0;
        int index = 0;
        while (true) {
            time++;

            // 머리 이동 준비
            int nr = head[0] + dr[snake[head[0]][head[1]][1]];
            int nc = head[1] + dc[snake[head[0]][head[1]][1]];

            // 머리가 범위 밖 or 몸통에 닿는지
            if (nr < 1 || nr > n || nc < 1 || nc > n || snake[nr][nc][0] == 1) {
                break;
            }

            // 머리 이동
            snake[nr][nc][0] = 1;
            snake[nr][nc][1] = snake[head[0]][head[1]][1];
            head[0] = nr;
            head[1] = nc;

            // 사과 없으면 꼬리 없앰
            if (!apple[nr][nc]) {
                int[] prev = {tail[0], tail[1]};
                snake[prev[0]][prev[1]][0] = 0;
                tail[0] = prev[0] + dr[snake[prev[0]][prev[1]][1]];
                tail[1] = prev[1] + dc[snake[prev[0]][prev[1]][1]];
            } else apple[nr][nc] = false;

            // 방향 확인
            if (index < l && dir[index].time == time) {
                if (snake[nr][nc][1] == 0 && dir[index].direction == 'L') snake[nr][nc][1] = 2;
                else if (snake[nr][nc][1] == 0 && dir[index].direction == 'D') snake[nr][nc][1] = 3;
                else if (snake[nr][nc][1] == 1 && dir[index].direction == 'L') snake[nr][nc][1] = 3;
                else if (snake[nr][nc][1] == 1 && dir[index].direction == 'D') snake[nr][nc][1] = 2;
                else if (snake[nr][nc][1] == 2 && dir[index].direction == 'L') snake[nr][nc][1] = 1;
                else if (snake[nr][nc][1] == 2 && dir[index].direction == 'D') snake[nr][nc][1] = 0;
                else if (snake[nr][nc][1] == 3 && dir[index].direction == 'L') snake[nr][nc][1] = 0;
                else if (snake[nr][nc][1] == 3 && dir[index].direction == 'D') snake[nr][nc][1] = 1;

                index++;
            }
        }

        System.out.println(time);
    }

    public static class Direction {
        public int time;
        public char direction;

        Direction(int t, char d) {
            this.time = t;
            this.direction = d;
        }
    }
}
