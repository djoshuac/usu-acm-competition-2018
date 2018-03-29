import java.util.*;
import java.io.*;

public final class Main {

    public static void main(String[] args) throws Exception {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String input = st.nextToken();

        int moves = 1;
        int i = 1;

        while(2*i <= input.length()){
            moves += input.substring(0, i).equals(input.substring(i, 2*i)) ? 1 : i;
            i*=2;
            if(2*i>input.length()){
                moves += input.length() - i;
            }
        }

        pw.println(moves);
        pw.close();
    }

}