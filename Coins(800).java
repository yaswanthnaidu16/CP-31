//If k is even and n is odd, representation is impossible; otherwise it is always possible

import java.util.*;
public class Codeforces {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
      
        while (t-- > 0) {
            long n = sc.nextLong();
            long k = sc.nextLong();

            if (k % 2 == 0 && n % 2 != 0) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }
    }
}
