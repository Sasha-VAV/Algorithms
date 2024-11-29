package YandexProfessionalPIT2024;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Task10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (!map.containsKey(a)) {
                map.put(a, new ArrayList<>());
            }
            map.get(a).add(b);
        }
    }
}
