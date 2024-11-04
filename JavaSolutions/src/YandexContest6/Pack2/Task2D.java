package YandexContest6.Pack2;

import java.io.File;
import java.io.IOException;
import java.util.*;

public class Task2D {
    public static void main(String[] args) throws IOException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        arr = Arrays.stream(arr).sorted().toArray();
        LinkedList<Integer> q = new LinkedList<>();
        for (int x: arr){
            if (!q.isEmpty() && x - q.getFirst() > k){
                q.removeFirst();
                q.addLast(x);
            }
            else{
                q.addLast(x);
            }

        }
        System.out.println(q.size());
    }
}
