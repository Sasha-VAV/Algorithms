package YandexContest6.Pack3;

import java.util.LinkedList;
import java.util.Scanner;

public class Task3A {
    public static void main(String[] args) {
        LinkedList<Character> list = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '{' || c == '(' || c == '[')
                list.add(c);
            else{
                if (list.isEmpty()){
                    System.out.println("no");
                    return;
                }
                char b = list.getLast();
                if (b == '}' || b == ')' || b == ']'){
                    System.out.println("no");
                    return;
                }
                switch (c){
                    case '}':
                        if (b != '{'){
                            System.out.println("no");
                            return;
                        }
                        break;
                    case ')':
                        if (b != '('){
                            System.out.println("no");
                            return;
                        }
                        break;
                    case ']':
                        if (b != '['){
                            System.out.println("no");
                            return;
                        }
                        break;
                    default:
                        System.out.println("no");
                        return;
                }
                list.removeLast();
            }
        }
        if (list.isEmpty()){
            System.out.println("yes");
        }
        else
            System.out.println("no");
    }
}
