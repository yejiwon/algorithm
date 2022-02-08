import java.util.Scanner;

public class Palindrome {

    public static String solution(String str) {
        int len = str.length();
        str = str.toUpperCase();

        for (int i = 0; i < len/2; i++) {
             if(str.charAt(i) != str.charAt(len-i-1))
                 return "NO";
        }
        return "YES";
    }

    public static String solution2(String str) {
        String strToCompare = new StringBuilder(str).reverse().toString();
        if (str.equals(strToCompare))
            return "YES";
        return "NO";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(solution(str));
    }
}
