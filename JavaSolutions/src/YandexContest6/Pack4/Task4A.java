package YandexContest6.Pack4;

import java.util.*;

public class Task4A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, MyTree> map = new TreeMap<>();
        MyTree lastTree = null;
        for (int i = 0; i < n - 1; i++) {
            String child = sc.next();
            String parent = sc.next();
            MyTree treeParent;
            if (!map.containsKey(parent)) {
                treeParent = new MyTree(parent);
                map.put(parent, treeParent);
            }
            else{
                treeParent = map.get(parent);
            }
            MyTree treeChild;
            if (map.containsKey(child)) {
                treeChild = map.get(child);
                treeChild.parent = treeParent;
            }
            else{
                treeChild = new MyTree(child, treeParent);
                map.put(child, treeChild);
            }
            treeParent.children.add(treeChild);
            if (i == n - 2)
                lastTree = treeParent;
        }
        if (lastTree == null) {
            return;
        }
        while (lastTree.parent != null){
            lastTree = lastTree.parent;
        }
        lastTree.updateLevels(-1);
        Set<String> keys = map.keySet();
        for (String key : keys) {
            System.out.println(key + " " + map.get(key).level);
        }
    }
}
class MyTree{
    public String name;
    public MyTree parent;
    public ArrayList<MyTree> children = new ArrayList<>();
    public int level = 0;
    public MyTree(String name) {
        this.name = name;
    }
    public MyTree(String name, MyTree parent) {
        this.name = name;
        this.parent = parent;
    }
    public void updateLevels(int parentLevel) {
        this.level = parentLevel + 1;
        for (MyTree child : children) {
            child.updateLevels(level);
        }
    }
}
