package nestnet_algorithm_2025_1_advanced.JeongHanUl.summer_week_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_13460 {
    //public class Main {

    static char[][] map;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int min = 100;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] in = br.readLine().split(" ");
        n = Integer.parseInt(in[0]);
        m = Integer.parseInt(in[1]);
        map = new char[n][m];
        for (int i = 0; i < n; i++) map[i] = br.readLine().toCharArray();

        int[] red = new int[2];
        int[] blue = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'R') {
                    red[0] = i;
                    red[1] = j;
                } else if (map[i][j] == 'B') {
                    blue[0] = i;
                    blue[1] = j;
                }
            }
        }

        dfs(red, blue, 0);

        if (min == 100) System.out.println(-1);
        else System.out.println(min);
    }

    static void dfs(int[] red, int[] blue, int cnt) {
        // 빨간 구슬만 구멍 통과 했는지 확인
        if ((red[0] == 0 && red[1] == 0) && (blue[0] != 0 && blue[1] != 0)) {
            min = Math.min(min, cnt);
            return;
        }

        // 종료 조건
        if ((blue[0] == 0 && blue[1] == 0) || cnt == 10) return;

        //상하좌우 기울이기
        for (int i = 0; i < 4; i++) {
            int redRow = red[0];
            int redCol = red[1];
            int blueRow = blue[0];
            int blueCol = blue[1];

            if (i == 0 && redRow < blueRow) move(red, blue, i);
            else if (i == 0) move(blue, red, i);
            else if (i == 1 && redRow > blueRow) move(red, blue, i);
            else if (i == 1) move(blue, red, i);
            else if (i == 2 && redCol < blueCol) move(red, blue, i);
            else if (i == 2) move(blue, red, i);
            else if (i == 3 && redCol > blueCol) move(red, blue, i);
            else if (i == 3) move(blue, red, i);

            dfs(red, blue, cnt + 1);
            red[0] = redRow;
            red[1] = redCol;
            blue[0] = blueRow;
            blue[1] = blueCol;
        }
    }

    static void move(int[] first, int[] second, int dir) {
        // 처음 이동
        int nr = first[0] + dr[dir];
        int nc = first[1] + dc[dir];
        while (true) {
            if (map[nr][nc] == '#') break;

            if (map[nr][nc] == 'O') {
                first[0] = 0;
                first[1] = 0;
                break;
            }

            first[0] = nr;
            first[1] = nc;
            nr += dr[dir];
            nc += dc[dir];
        }

        // 다음 이동
        nr = second[0] + dr[dir];
        nc = second[1] + dc[dir];
        while (true) {
            if (map[nr][nc] == '#' || (nr == first[0] && nc == first[1])) break;

            if (map[nr][nc] == 'O') {
                second[0] = 0;
                second[1] = 0;
                break;
            }

            second[0] = nr;
            second[1] = nc;
            nr += dr[dir];
            nc += dc[dir];
        }
    }
}
