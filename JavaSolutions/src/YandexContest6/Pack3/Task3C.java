package YandexContest6.Pack3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Scanner;


public class Task3C {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int n = sc.nextInt();
        int k = sc.nextInt();
        LinkedList<Integer> list = new LinkedList<>();
        LinkedList<Integer> minQueue = new LinkedList<>();
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            if (i < k){
                list.add(a);
                while (!minQueue.isEmpty() && minQueue.getLast() > a){
                    minQueue.removeLast();
                }
                minQueue.add(a);
                if (i == k - 1){
                    answer.append(minQueue.getFirst()).append("\n");
                }
            }
            else {
                int b = list.removeFirst();
                list.add(a);
                if (minQueue.getFirst() == b){
                    minQueue.removeFirst();
                }
                while (!minQueue.isEmpty() && minQueue.getLast() > a){
                    minQueue.removeLast();
                }
                minQueue.add(a);
                answer.append(minQueue.getFirst()).append("\n");
            }
        }
        System.out.println(answer);
    }
}
