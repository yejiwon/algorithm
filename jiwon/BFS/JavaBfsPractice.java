import java.util.LinkedList;
import java.util.Queue;

public class JavaBfsPractice {
    // BFS
    public static class Problem11 {
        static int[] dx = { -1, 0, 1, 0 };
        static int[] dy = { 0, 1, 0, -1 };
        static int[][] board, dis;

        class Point {
            public int x, y;

            public Point(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }

        public void set() {
            board = new int[8][8];
            dis = new int[8][8];
        }

        public void BFS(int x, int y) {
            Queue<Point> queue = new LinkedList<>();
            queue.offer(new Point(x, y));
            board[x][y] = 1;

            while (!queue.isEmpty()) {
                Point now = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];
                    if (nx >= 1 && nx <= 7 && ny >= 1 && ny <= 7 && board[nx][ny] == 0) {
                        board[nx][ny] = 1;
                        queue.offer(new Point(nx, ny));
                        dis[nx][ny] = dis[now.x][now.y] + 1;
                    }
                }
            }
        }
    }

    // BFS
    public static class Problem12 {
        static int NOT_RIPE_TOMATO = 0;
        static int RIPE_TOMATO = 1;
        static int EMPTY = -1;

        static int[] dx = { -1, 0, 1, 0 };
        static int[] dy = { 0, 1, 0, -1 };
        static int n, m;
        static int[][] board;
        static int[][] day;
        static Queue<Point> queue = new LinkedList<>();

        class Point {
            public int x, y;

            public Point(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }

        public void BFS() {
            while (!queue.isEmpty()) {
                Point now = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && board[nx][ny] == NOT_RIPE_TOMATO) {
                        board[nx][ny] = RIPE_TOMATO;
                        queue.offer(new Point(nx, ny));
                        day[nx][ny] = day[now.x][now.y] + 1;
                    }
                }
            }

        }

        public int solution(int[][] board) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j] == RIPE_TOMATO) {
                        queue.offer(new Point(i, j));
                    }
                }
            }
            BFS();

            int ans = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    ans = Math.max(ans, day[i][j]);
                    if (board[i][j] == NOT_RIPE_TOMATO) {
                        return -1;
                    }
                }
            }

            return ans;
        }
    }

    // BFS
    public static class Problem13 {
        static int[] dx = { -1, 0, 1, 0 };
        static int[] dy = { 0, 1, 0, -1 };

        static int SEA = 0;
        static int ISLAND = 1;

        static int islandNum = 0;
        static int[][] board;
        static int n, m;

        class Point {
            int x, y;

            public Point(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }

        public void bfs(int x, int y) {
            Queue<Point> queue = new LinkedList<>();
            queue.offer(new Point(x, y));

            while (!queue.isEmpty()) {
                Point now = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];

                    if (nx >= 0 && nx < n && ny >= 0 && ny > m && board[nx][ny] == ISLAND) {
                        queue.offer(new Point(nx, ny));
                        board[nx][ny] = SEA;
                    }
                }
            }
        }

        public int solution() {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j] == ISLAND) {
                        bfs(i, j);
                        islandNum += 1;
                    }
                }
            }

            return islandNum;
        }
    }
}
