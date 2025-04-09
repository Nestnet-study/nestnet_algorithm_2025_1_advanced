package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class boj_6987 {
    //public class Main {

    static int[] result = new int[4];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][][] input = new int[4][6][3];
        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 6; j++) {
                for (int k = 0; k < 3; k++) input[i][j][k] = Integer.parseInt(st.nextToken());
            }
        }

        List<int[]> combination = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) combination.add(new int[]{i, j});
        }

        for (int i = 0; i < 4; i++) {
            dfs(combination, 0, input[i], i);
        }

        for (int i : result) System.out.print(i + " ");
    }

    static void dfs(List<int[]> combination, int depth, int[][] target, int index) {
        // 베이스 컨디션
        if (depth == 15) {
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    if (target[i][j] != 0) return;
                }
            }

            result[index] = 1;
            return;
        }

        // 가지 치기
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) if (target[i][j] < 0) return;
        }

        int[] team = combination.get(depth);

        // [0]이 이김
        target[team[0]][0]--;
        target[team[1]][2]--;
        dfs(combination, depth + 1, target, index);
        target[team[0]][0]++;
        target[team[1]][2]++;

        // 비김
        target[team[0]][1]--;
        target[team[1]][1]--;
        dfs(combination, depth + 1, target, index);
        target[team[0]][1]++;
        target[team[1]][1]++;

        // [0]이 짐
        target[team[0]][2]--;
        target[team[1]][0]--;
        dfs(combination, depth + 1, target, index);
        target[team[0]][2]++;
        target[team[1]][0]++;
    }
}
