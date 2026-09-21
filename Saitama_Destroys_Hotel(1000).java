import java.util.*;
public class Main {
    public static void main(String[] args) {
      
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int a = 0;

        for (int i = 0; i < n; i++) {
            int f = sc.nextInt();
            int t = sc.nextInt();
            int x = Math.max(s - f, t) + f;
            a = Math.max(a, x);
        }
        System.out.println(a);
    }
}
