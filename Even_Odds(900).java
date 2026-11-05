import java.util.*;
class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();

        long c = (a + 1) / 2;

        if(b <= c)
        {
            System.out.println(2 * b - 1);
        }
        else
        {
            System.out.println(2 * (b - c));
        }
    }
}
