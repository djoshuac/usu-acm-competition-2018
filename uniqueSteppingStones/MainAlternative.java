import java.util.*;
import java.io.*;

public final class MainAlternative {

    public static void main(String[] args) throws Exception {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Set<Integer>> list = new ArrayList<>(m);

        for(int i = 0; i<m; i++){
            list.add(new HashSet<>());
        }

        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<m; j++){
                int val = Integer.parseInt(st.nextToken());
                list.get(j).add(val);
            }
        }

        pw.println(containsUniquePath(list, 0, new HashSet<Integer>()) ? "Yes" : "No");
        pw.close();
    }

    public static boolean containsUniquePath(List<Set<Integer>> list, int row, Set<Integer> set){
        if(row >= list.size())
            return set.size() == list.size();

        for(int i : list.get(row)){
            if(set.contains(i))
                continue;
            set.add(i);
            if(containsUniquePath(list, row+1, set))
                return true;
            set.remove(i);
        }

        return false;
    }
}
