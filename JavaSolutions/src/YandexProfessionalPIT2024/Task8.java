package YandexProfessionalPIT2024;

import java.util.*;

public class Task8 {
    static int Square(int n, int b){
        int a = n;
        int sq = 0;
        while (a > 0){
            int pow = a % b;
            sq += pow * pow;
            a = a / b;
        }
        return sq;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int b = sc.nextInt();
        ArrayList<Pair> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = Square(x, b);
            list.add(new Pair(x, y));
        }
        list.sort(Comparator.comparing(Pair::getB));
        StringBuilder ans = new StringBuilder();
        for (Pair pair : list) {
            ans.append(pair.a).append(" ");
        }
        System.out.println(ans);
    }
}

class Pair{
    public int a;
    public int b;
    Pair(int a, int b){
        this.a = a;
        this.b = b;
    }
    public int getB(){
        return b;
    }
}