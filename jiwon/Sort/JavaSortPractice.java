import java.util.ArrayList;
import java.util.Collections;

public class JavaSortPractice {
    // 좌표 정렬
    class Problem7 {
        class Point implements Comparable<Point> {
            public int x, y;

            public Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

            @Override
            public int compareTo(Point o) {
                // 오름차순 정렬
                if (this.x == o.x)
                    return this.y - o.y;
                else
                    return this.x - o.x;

                // 내림차순 정렬
                // if (this.x == o.x) return o.y - this.y;
                // else return o.x - this.x;
            }
        }

        public void solution() {
            ArrayList<Point> arr = new ArrayList<>();
            arr.add(new Point(1, 2));
            arr.add(new Point(3, 5));
            arr.add(new Point(1, 6));

            Collections.sort(arr);

            for (Point point : arr) {
                System.out.println(point.x + point.y);
            }
        }
    }
}
