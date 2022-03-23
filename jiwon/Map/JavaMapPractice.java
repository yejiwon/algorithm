import java.util.HashMap;

public class JavaMapAlgorithm {

    class Problem1 {

        char solution(String str) {

            HashMap<Character, Integer> hashMap = new HashMap<>();
            for (char s : str.toCharArray()) {
                hashMap.put(s, hashMap.getOrDefault(s, 0) + 1);
            }

            char answer = ' ';
            int maxVal = 0;
            for (char key : hashMap.keySet()) {
                if (hashMap.get(key) > maxVal) {
                    maxVal = hashMap.get(key);
                    answer = key;
                }
            }

            return answer;
        }

    }

}
