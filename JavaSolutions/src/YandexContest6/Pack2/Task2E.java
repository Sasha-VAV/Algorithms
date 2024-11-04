package YandexContest6.Pack2;

import java.util.Arrays;
import java.util.Scanner;

public class Task2E {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        //long startTime = System.nanoTime();
        arr = Arrays.stream(arr).sorted().toArray();
        int a = n;
        //System.out.println((System.nanoTime() - startTime) / 1000000);
        int b = -1;
        StringBuilder answer = new StringBuilder();
        if (a % 2 == 1) {
            answer.append(arr[a / 2]).append(" ");
            a = a / 2 - 1;
            b = a + 2;
        }
        else {
            a = a / 2 - 1;
            b = a + 1;
        }
        while (b < n){
            answer.append(arr[a]).append(" ").append(arr[b]).append(" ");
            a--;
            b++;
        }
        System.out.println(answer);
        //System.out.println((System.nanoTime() - startTime) / 1000000);
    }
}
