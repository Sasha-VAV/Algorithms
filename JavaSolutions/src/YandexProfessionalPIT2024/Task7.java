package YandexProfessionalPIT2024;

import java.util.Scanner;

public class Task7 {
    public static void main(String[] args) {
        int C;
        Scanner sc = new Scanner(System.in);
        C = sc.nextInt();
        for (int i = 0; i < C; i++) {
            int t1 = sc.nextInt();
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int t2 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            if ((t2 - t1) < 100)
                System.out.println(1);
            else if ((t2 - t1) >= 100) {
                double a = Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
                if (a <= 50){
                    if ((t2 - t1) <= 1000)
                        System.out.println(2);
                    else
                        System.out.println(3);
                }
                else {
                    System.out.println(4);
                }
            }
        }
    }
}
