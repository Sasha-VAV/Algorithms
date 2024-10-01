import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class L2933 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("a");
        list.add("0549");
        List<List<String>> lists = new ArrayList<>();
        lists.add(list);
        list = new ArrayList<String>();
        list.add("b");
        list.add("0457");
        lists.add(list);
        list = new ArrayList<String>();
        list.add("a");
        list.add("0532");
        lists.add(list);
        list = new ArrayList<String>();
        list.add("a");
        list.add("0621");
        lists.add(list);
        list = new ArrayList<String>();
        list.add("b");
        list.add("0540");
        lists.add(list);

        Solution solution = new Solution();
        System.out.println(solution.findHighAccessEmployees(lists));
    }

    private static class Solution {
        public boolean check(List<String> strings){
            if (strings.size() < 3)
                return false;
            for (int i = 2; i < strings.size(); i++) {
                if (Integer.parseInt(strings.get(i)) < 100 + Integer.parseInt(strings.get(i - 2)))
                    return true;
            }
            return false;
        }
        public List<String> findHighAccessEmployees(List<List<String>> access_times) {
            List<String> high_access_times = new ArrayList<>();
            HashMap<String, List<String>> map = new HashMap<>();
            for (List<String> access_time : access_times) {
                if (!high_access_times.contains(access_time.getFirst())) {
                    List<String> accessTime = map.get(access_time.getFirst());
                    if (accessTime == null) {
                        accessTime = new ArrayList<>();
                    }
                    accessTime.add(access_time.getLast());
                    accessTime.sort(String::compareTo);
                    if (check(accessTime)) {
                        high_access_times.add(access_time.getFirst());
                    }
                    map.put(access_time.getFirst(), accessTime);
                }
            }
            return high_access_times;
        }
    }

}



