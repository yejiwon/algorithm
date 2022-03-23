import java.util.ArrayList;
import java.util.Collections;

public class JavaGreedyPractice {

    class problem1 {
        class Person implements Comparable<Person> {
            int h, w;

            public Person(int h, int w) {
                this.h = h;
                this.w = w;
            }

            @Override
            public int compareTo(Person o) {
                if (this.h == o.h)
                    return o.w - this.w;
                else
                    return o.h - this.h;
            }
        }

        public int solution(ArrayList<Person> arr, int n) {
            int maxWeight = 0;
            int cnt = 0;
            Collections.sort(arr);

            for (Person person : arr) {
                if (person.w > maxWeight) {
                    cnt += 1;
                    maxWeight = person.w;
                }
            }

            return cnt;
        }
    }

    // 회의 최대한 많이 -> 먼저 끝나는 것(그 다음 시작 시간) 순으로 선택하면 됨
    class Problem2 {
        class Meeting implements Comparable<Meeting> {
            int s, e;

            public Meeting(int s, int e) {
                this.s = s;
                this.e = e;
            }

            @Override
            public int compareTo(Meeting o) {
                if (this.e == o.e)
                    return this.s - o.s;
                else
                    return this.s - o.s;
            }
        }

        public int solution(ArrayList<Meeting> meetings) {
            int now = 0;
            int cnt = 0;
            Collections.sort(meetings);

            for (Meeting meeting : meetings) {
                if (meeting.s >= now)
                    cnt += 1;
            }

            return cnt;
        }
    }
}
