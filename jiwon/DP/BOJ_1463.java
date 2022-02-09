import java.util.Scanner;

public class BOJ_1463 {

    public static int solution(int N, int[] dp) {
        for(int i=2; i<=N; i++) {
            dp[i] = dp[i-1] + 1;
            if (i % 3 == 0)
                dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
            if (i % 2 == 0)
                dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
        }

        return dp[N];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N+1];
        System.out.println(solution(N, dp));
    }
}
