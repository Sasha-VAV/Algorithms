package YandexContest6.Pack3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Task3E {
    static Integer calc(String[] s){
        LinkedList<Integer> list = new LinkedList<>();
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
        return list.removeLast();
    }
    static String[] toPostfix(String s) throws Exception {
        ArrayList<String> ans = new ArrayList<>();
        LinkedList<Character> stack = new LinkedList<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '+' -> {
                    while (!stack.isEmpty() &&  (stack.getLast() == '*' || stack.getLast() == '+' || stack.getLast() == '-')) {
                        ans.add(stack.removeLast().toString());
                    }
                    stack.addLast(c);
                }
                case '-' -> {
                    while (!stack.isEmpty() &&  (stack.getLast() == '*' || stack.getLast() == '-' || stack.getLast() == '+')) {
                        ans.add(stack.removeLast().toString());
                    }
                    stack.addLast(c);
                }
                case '*' -> {
                    while (!stack.isEmpty() && stack.getLast() == '*'){
                        ans.add(stack.removeLast().toString());
                    }
                    stack.addLast(c);
                }
                case '(' -> {
                    stack.addLast(c);
                }
                case ')' -> {
                    while (!stack.isEmpty() && stack.getLast() != '('){
                        ans.add(stack.removeLast().toString());
                    }
                    stack.removeLast();
                }
                default -> {
                    if (!Character.isDigit(c) && c != ' '){
                        throw new Exception("Invalid character");
                    }
                    if (c == ' '){
                        break;
                    }
                    if (i == 0){
                        ans.add(String.valueOf(c));
                        break;
                    }
                    if (Character.isDigit(s.charAt(i-1))){
                        ans.set(ans.size() - 1, ans.getLast() + c);
                        break;
                    }
                    ans.add(String.valueOf(c));
                }
            }
        }
        while (!stack.isEmpty()){
            ans.add(stack.removeLast().toString());
        }
        String[] res = new String[ans.size()];
        for (int i = 0; i < ans.size(); i++){
            res[i] = ans.get(i);
        }
        return res;
    }
    static boolean checkIfStringIsValid(String s){
        LinkedList<Character> stack = new LinkedList<>();
        s = s.replaceAll("1", "0");
        s = s.replaceAll("2", "0");
        s = s.replaceAll("3", "0");
        s = s.replaceAll("4", "0");
        s = s.replaceAll("5", "0");
        s = s.replaceAll("6", "0");
        s = s.replaceAll("7", "0");
        s = s.replaceAll("8", "0");
        s = s.replaceAll("9", "0");
        s = s.replaceAll("\\s+", " ");
        if (s.contains("0 0"))
            return false;
        s = s.replaceAll(" ", "");
        if (s.contains("(*0") || s.startsWith("*0"))
            return false;
        s = s.replaceAll("-", "+");
        s = s.replaceAll("\\*", "+");
        if (s.contains("++") || s.contains("0(") || s.contains(")0"))
            return false;
        s = s.replaceAll("0", "");
        s = s.replaceAll("\\+", "");
        for (char c : s.toCharArray()){
            switch (c){
                case  '(' -> stack.addLast(c);
                case ')' -> {
                    if (stack.isEmpty() || stack.getLast() != '('){
                        return false;
                    }
                    stack.removeLast();
                }
                default -> {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    static String prepareString(String s){
        if (s.isEmpty())
            return s;
        s = s.trim();
        if (s.charAt(0) != '(' && s.charAt(0) != '*')
            s = "0" + s;
        s = s.replaceAll("\\(-", "(0-");
        return s;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        s = prepareString(s);
        if (checkIfStringIsValid(s)){
            s = s.replaceAll("\\s+", "");
            try {
                System.out.println(calc(toPostfix(s)));
            }
            catch (Exception e) {
                System.out.println("WRONG");
            }
        }
        else
            System.out.println("WRONG");
    }
}
