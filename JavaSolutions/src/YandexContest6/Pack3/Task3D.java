package YandexContest6.Pack3;

import java.util.LinkedList;
import java.util.Scanner;

public class Task3D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<>();
        String[] s = sc.nextLine().split(" ");
        for (String str : s) {
            switch (str) {
                case "+" -> {
                    Integer a = list.removeLast();
                    a += list.removeLast();
                    list.addLast(a);
                }
                case "-" -> {
                    Integer a = list.removeLast();
                    a = list.removeLast() - a;
                    list.addLast(a);
                }
                case "*" -> {
                    Integer a = list.removeLast();
                    a *= list.removeLast();
                    list.addLast(a);
                }
                default -> list.addLast(Integer.parseInt(str));
            }
        }
        System.out.println(list.removeLast());
    }
}
