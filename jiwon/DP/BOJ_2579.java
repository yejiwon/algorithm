import java.util.Scanner;

public class BOJ_2579 {

    public static int solution(int[] stair, int[] dp, int N) {
        dp[1] = stair[1];
        dp[2] = stair[1] + stair[2];
        dp[3] = Math.max(stair[1], stair[2]) + stair[3];

        for (int n = 4; n <= N; n++) {
            dp[n] = Math.max(dp[n - 3] + stair[n - 1], dp[n - 2]) + stair[n];
        }

        return dp[N];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] stair = new int[N+1];
        int[] dp = new int[N+1];
        for (int i = 1; i <= N; i++)
            stair[i] = sc.nextInt();

        System.out.println(solution(stair, dp, N));
    }
}



