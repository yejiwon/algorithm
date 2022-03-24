public class JavaDfsPractice {

    public static class Problem1 {
        static int n, total = 0;

        public String DFS(int L, int sum, int[] arr) {
            if (L == n) {
                if ((total - sum) == sum)
                    return "YES";
            } else {
                DFS(L + 1, sum + arr[L], arr);
                DFS(L + 1, sum, arr);
            }
            return "NO";
        }
    }

    public static class Problem2 {
        static int c, n;
        static int maxVal = 0;

        public void DFS(int level, int sumVal, int[] arr) {
            if (level == n) {
                maxVal = Math.max(sumVal, maxVal);
            } else {
                DFS(level + 1, sumVal + arr[level], arr);
                DFS(level + 1, sumVal, arr);
            }
        }
    }

    public static class Problem3 {
        static int n, m;
        static int maxScore = 0;

        public void DFS(int level, int score, int time, int[] ps, int[] pt) {
            if (time > m)
                return;
            if (level == n) {
                maxScore = Math.max(maxScore, score);
            } else {
                DFS(level + 1, score + ps[level], time + pt[level], ps, pt);
                DFS(level + 1, score, time, ps, pt);
            }
        }

    }

    // 중복 순열
    public static class Problem4 {

        static int[] ans;
        static int n, m;

        public void DFS(int level) {
            if (level == m) {
                for (int x : ans)
                    System.out.print(x + " ");
                System.out.println();
            } else {
                for (int i = 1; i <= n; i++) {
                    ans[level] = i;
                    DFS(level + 1);
                }
            }
        }

    }

    public static class Problem5 {
        static int minVal = Integer.MAX_VALUE;
        static int n, m;
        static Integer[] coins;

        // Arrays.sort(arr, Collections.reverseOrder();

        public void DFS(int level, int sum, Integer[] coins) {
            if (sum > m)
                return;
            if (level >= minVal)
                return;
            if (sum == m) {
                minVal = Math.min(minVal, sum);
            } else {
                for (int i = 0; i < n; i++) {
                    DFS(level + 1, sum + coins[i], coins);
                }
            }
        }
    }

    // 순열
    public static class Problem6 {
        static int[] ans, ch, arr;
        static int n, m;

        public void DFS(int level) {
            if (level == m) {
                for (int x : ans)
                    System.out.print(x);
                System.out.println();
            } else {
                for (int i = 0; i < n; i++) {
                    if (ch[i] == 0) {
                        ch[i] = 1;
                        ans[level] = arr[i];
                        DFS(level + 1);
                        ch[i] = 0;
                    }
                }
            }
        }
    }
}
