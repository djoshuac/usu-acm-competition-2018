import java.util.*;
import java.io.*;

public final class Main {

    public static void main(String[] args) throws Exception {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] stones = new int[n][m];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int val = Integer.parseInt(st.nextToken());
                stones[i][j] = val;
            }
        }

        pw.println(containsUniquePath(stones) ? "Yes" : "No");
        pw.close();
    }

    public static boolean containsUniquePath(int[][] arr){

        int[] rowTracker = new int[arr[0].length];
        int currRow = 0;
        int currCol = 0;
        Stack<Integer> lastAdded = new Stack<>();
        Set<Integer> seenSet = new HashSet<>();

        while(currCol >= 0 && currCol < arr[0].length){
            currRow = rowTracker[currCol];
            if(currRow >= arr.length){
                if(!seenSet.isEmpty())
                    seenSet.remove(lastAdded.pop());
                rowTracker[currCol] = 0;
                if(currCol > 0)
                    rowTracker[currCol-1]++;
                currCol--;
                continue;
            }

            int currStone = arr[currRow][currCol];

            if(seenSet.contains(currStone)){
                rowTracker[currCol]++;
                continue;
            }

            seenSet.add(currStone);
            lastAdded.push(currStone);
            currCol++;

            if(seenSet.size() == arr[0].length)
                return true;
        }

        return false;
    }
}