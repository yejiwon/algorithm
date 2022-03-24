public class JavaDpPractice {

    // 계단 오르기 : 한계단 또는 두계단씩 올라갈 수 있음 이떄, N 계단을 오르는 방법의 수
    static class Problem1 {
        static int[] memo;

        public int solution(int n) {
            memo[1] = 1;
            memo[2] = 2;

            for (int i = 3; i <= n; i++) {
                memo[i] = memo[i - 1] + memo[i - 2];
            }
            return memo[n];
        }
    }

    // 최대 부분 증가 수열
    static class Problem2 {
        static int[] memo;

        public int solution(int[] arr, int n) {
            int ans = 0;

            for (int i = 0; i < n; i++) {
                int maxVal = 0;
                for (int j = n - 1; j >= 0; j--) {
                    if (arr[n] > arr[j] && memo[j] > maxVal)
                        maxVal = memo[j] + 1;
                }
                memo[i] = maxVal + 1;
                ans = Math.max(ans, memo[i]);
            }

            return ans;
        }
    }
}