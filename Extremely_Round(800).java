//Count numbers from 1 to n that contain exactly one non-zero digit

import java.util.*;
public class Codeforces {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            String n = sc.next();
            int ans = (n.length() - 1) * 9 + (n.charAt(0) - '0');
            System.out.println(ans);
        }
    }
}
