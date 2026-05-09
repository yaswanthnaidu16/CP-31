//Find the minimum absolute value since converting that element to 0 needs the fewest operations

import java.util.*;
public class codeforces {
    public static void main(String[] args) {
      
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            ans = Math.min(ans, Math.abs(x));
        }
        System.out.println(ans);
    }
}
