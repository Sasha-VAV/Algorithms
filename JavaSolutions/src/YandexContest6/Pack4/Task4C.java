package YandexContest6.Pack4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Task4C {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int n = sc.nextInt();
        Map<String, MyTree3> map = new TreeMap<>();
        MyTree3 lastTree = null;
        for (int i = 0; i < n - 1; i++) {
            String child = sc.next();
            String parent = sc.next();
            MyTree3 treeParent;
            if (!map.containsKey(parent)) {
                treeParent = new MyTree3(parent);
                map.put(parent, treeParent);
            }
            else{
                treeParent = map.get(parent);
            }
            MyTree3 treeChild;
            if (map.containsKey(child)) {
                treeChild = map.get(child);
                treeChild.parent = treeParent;
            }
            else{
                treeChild = new MyTree3(child, treeParent);
                map.put(child, treeChild);
            }
            treeParent.children.add(treeChild);
        }

        while (sc.hasNext()) {
            String name1 = sc.next();
            String name2 = sc.next();
            Map<String, MyTree3> curr_map = new HashMap<>();
            MyTree3 first = map.get(name1);
            MyTree3 second = map.get(name2);
            while (first != null) {
                curr_map.put(first.name, first);
                first = first.parent;
            }
            while (second != null) {
                if (curr_map.containsKey(second.name)) {
                    System.out.println(second.name);
                    break;
                }
                second = second.parent;
            }
        }
    }
}
class MyTree3 {
    public String name;
    public MyTree3 parent;
    public ArrayList<MyTree3> children = new ArrayList<>();
    public MyTree3(String name) {
        this.name = name;
    }
    public MyTree3(String name, MyTree3 parent) {
        this.name = name;
        this.parent = parent;
    }
}
