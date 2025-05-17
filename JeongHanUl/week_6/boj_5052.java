package nestnet_algorithm_2025_1_advanced.JeongHanUl.week_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class boj_5052 {
    //public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] input = new String[n];
            for (int i = 0; i < n; i++) input[i] = br.readLine();

            Arrays.sort(input);

            Trie trie = new Trie();
            boolean output = true;
            for (int i = 0; i < n; i++) {
                if (!trie.insert(input[i])) {
                    output = false;
                    break;
                }
            }

            System.out.println(output ? "YES" : "NO");
        }
    }

    static class Node {
        Map<Character, Node> children = new HashMap<>();
        boolean isEnd = false;
    }
    static class Trie {
        Node root = new Node();

        boolean insert(String str) {
            Node current = root;

            for (char ch : str.toCharArray()) {
                if (current.isEnd) return false;

                current = current.children.computeIfAbsent(ch, c -> new Node());
            }

            if (!current.children.isEmpty()) return false;

            current.isEnd = true;
            return true;
        }
    }
}
