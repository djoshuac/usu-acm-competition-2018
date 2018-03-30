import java.util.*;
import java.io.*;

public final class MainAlternative {

    public static void main(String[] args) throws Exception {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> list = new ArrayList<>();
        for(int i = 0; i<m; i++){
            list.add(new ArrayList<>());
        }

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int val = Integer.parseInt(st.nextToken());
                list.get(j).add(val);
            }
        }

        pw.println(containsUniquePathRecursive(list, m) ? "Yes" : "No");
        pw.close();
    }
    
    public static boolean containsUniquePathRecursive(List<List<Integer>> matchList, int targetLen){
        for(int i = 0; i<matchList.get(0).size(); i++){
            Set<Integer> set = new HashSet<>();
            set.add(matchList.get(0).get(i));
            if(checkForUniquePathRecurseHelper(matchList, set, 1, targetLen))
                return true;
            set.remove(matchList.get(0).get(i));
        }
        return false;
    }

    public static boolean checkForUniquePathRecurseHelper(List<List<Integer>> list, Set<Integer> set, int index, int targetSetLen){
        if(index >= list.size())
            return set.size() == targetSetLen;

        boolean res = false;
        for(int i = 0; i<list.get(index).size(); i++){
            int currVal = list.get(index).get(i);
            if(set.contains(currVal))
                continue;
            set.add(currVal);
            if(set.size() == targetSetLen)
                return true;
            res = checkForUniquePathRecurseHelper(list, set, index+1, targetSetLen);
            set.remove(currVal);
        }

        return set.size() == targetSetLen || res;
    }
}