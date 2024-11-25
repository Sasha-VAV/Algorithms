package YandexContest6.Pack4;

import java.util.*;

public class Task4B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, MyTree2> map = new TreeMap<>();
        MyTree2 lastTree = null;
        for (int i = 0; i < n - 1; i++) {
            String child = sc.next();
            String parent = sc.next();
            MyTree2 treeParent;
            if (!map.containsKey(parent)) {
                treeParent = new MyTree2(parent);
                map.put(parent, treeParent);
            }
            else{
                treeParent = map.get(parent);
            }
            MyTree2 treeChild;
            if (map.containsKey(child)) {
                treeChild = map.get(child);
                treeChild.parent = treeParent;
            }
            else{
                treeChild = new MyTree2(child, treeParent);
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
        lastTree.updateLevels();
        Set<String> keys = map.keySet();
        for (String key : keys) {
            System.out.println(key + " " + map.get(key).level);
        }
    }
}
class MyTree2 {
    public String name;
    public MyTree2 parent;
    public ArrayList<MyTree2> children = new ArrayList<>();
    public int level = 0;
    public MyTree2(String name) {
        this.name = name;
    }
    public MyTree2(String name, MyTree2 parent) {
        this.name = name;
        this.parent = parent;
    }
    public void updateLevels() {
        level = 0;
        for (MyTree2 child : children) {
            child.updateLevels();
            level += child.level + 1;
        }
    }
}
