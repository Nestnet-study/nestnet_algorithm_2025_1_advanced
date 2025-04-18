package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj_14891 {
    //public class Main {

    static char[][] gear = new char[5][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 1; i <= 4; i++) gear[i] = br.readLine().toCharArray();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            List<int[]> list = new ArrayList<>();
            list.add(new int[]{number, dir});

            // 왼쪽 판단
            boolean flag = true;
            int left = number - 1;
            int leftDir = dir;
            while (flag && left >= 1) {
                if (gear[left][2] == gear[left + 1][6]) {
                    flag = false;
                    continue;
                }

                leftDir = leftDir == 1 ? -1 : 1;
                list.add(new int[]{left, leftDir});
                left--;
            }

            // 오른쪽 판단
            flag = true;
            int right = number + 1;
            int rightDir = dir;
            while (flag && right <= 4) {
                if (gear[right][6] == gear[right - 1][2]) {
                    flag = false;
                    continue;
                }

                rightDir = rightDir == 1 ? -1 : 1;
                list.add(new int[]{right, rightDir});
                right++;
            }

            // 돌리기
            for (int[] k : list) spin(k[0], k[1]);
        }

        int sum = 0;
        for (int i = 1; i <= 4; i++) {
            if (gear[i][0] == '0') continue;

            sum += (int) Math.pow(2, i - 1);
        }

        System.out.println(sum);
    }

    // 시계방향이 1
    static void spin(int number, int dir) {
        // 반시계 방향
        if (dir == -1) {
            char temp = gear[number][0];
            for (int i = 0; i < 7; i++) {
                gear[number][i] = gear[number][i + 1];
            }
            gear[number][7] = temp;
        }

        // 시계 방향
        else {
            char temp = gear[number][7];
            for (int i = 7; i > 0; i--) {
                gear[number][i] = gear[number][i - 1];
            }
            gear[number][0] = temp;
        }
    }
}
