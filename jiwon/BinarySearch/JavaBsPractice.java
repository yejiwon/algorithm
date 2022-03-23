import java.util.Arrays;

public class JavaBsPractice {
    // binary search
    class problem8 {

        public void solution(int[] numbers, int target) {
            // 1. sort
            Arrays.sort(numbers);
            int lt = 0;
            int rt = numbers.length - 1;

            // 2. binary search
            while (lt <= rt) {
                int mid = (lt + rt) / 2;
                if (numbers[mid] == target)
                    break;
                if (numbers[mid] > target)
                    rt = mid - 1;
                else
                    lt = mid + 1;
            }
        }

    }
}
