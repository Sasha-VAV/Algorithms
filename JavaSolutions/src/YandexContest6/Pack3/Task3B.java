package YandexContest6.Pack3;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Task3B {
    static class P{
        public int a, b;
        public P(int a, int b){
            this.a = a;
            this.b = b;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
        LinkedList<P> linkedList = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            int x = list.get(i);
            while (!linkedList.isEmpty() && linkedList.getLast().a > x)
            {
                P p = linkedList.removeLast();
                list.set(p.b, i);
            }
            linkedList.add(new P(x,i));
        }
        while (!linkedList.isEmpty()){
            P p = linkedList.removeLast();
            list.set(p.b, -1);
        }
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            answer.append(list.get(i));
            if (i != n - 1)
                answer.append(" ");
        }
        System.out.println(answer);
    }
}
