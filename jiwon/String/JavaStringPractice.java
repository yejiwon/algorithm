public class JavaStringPractice {

    // 특정 문자를 입력받아 해당 특정문자가 입력받은 문자열에 몇 개 존재
    int countChar(String str, char letter) {
        int count = 0;
        str = str.toUpperCase();
        for (char s : str.toCharArray()) { // for-each문에는 iterator만 들어갈 수 있음
            if (s == letter) {
                count += 1;
            }
        }
        return count;
    }

    // 대->소 소->대 변경하기
    String convert(String str) {
        String ans = "";
        for (char s : toString().toCharArray()) {
            if (Character.isLowerCase(s)) { // character LowerCase 판별
                ans += Character.toUpperCase(s);
            } else {
                ans += Character.toLowerCase(s);
            }
        }
        return ans;
    }

    // 한 개의 문장이 주어지면 그 문장 속에서 가장 긴 단어 출력
    String getLongestWord(String str) {
        // 1번 : split
        // String answer = "";
        // int maxVal = Integer.MIN_VALUE;
        // String[] s = str.split(" ");
        // for (String word : s) {
        // if (word.length() > maxVal) {
        // maxVal = word.length();
        // answer = word;
        // }
        // }
        // return answer;

        // 2번 : indexOf, substring
        String answer = "";
        int maxVal = Integer.MIN_VALUE, pos;

        while ((pos = str.indexOf(" ")) != -1) {
            String tmp = str.substring(0, pos);
            if (tmp.length() > maxVal) {
                maxVal = tmp.length();
                answer = tmp;
            }
            str = str.substring(pos + 1); // n부터 끝까지 -> substring(n)
        }

        return answer;
    }

    // 단어 뒤집기
    String reverseString(String str) {
        // 1. Stringbuilder.reverser()
        // String ans = new StringBuilder(str).reverse().toString();
        // return ans;

        // 2. 배열 -> 포인터
        char[] array = str.toCharArray();
        int lt = 0;
        int rt = str.length() - 1;
        while (lt < rt) {
            char tmp = array[lt];
            array[lt] = array[rt];
            array[rt] = tmp;

            lt++;
            rt--;
        }
        return String.valueOf(array); // charArray -> string
    }

    // 특정 문자만 뒤집기
    String reverseString2(String str) {
        String answer = "";
        char[] array = str.toCharArray();
        int lt = 0;
        int rt = str.length() - 1;

        while (lt < rt) {
            if (!Character.isAlphabetic(array[lt])) {
                lt++;
            } else if (!Character.isAlphabetic(array[rt])) {
                rt++;
            } else {
                char tmp = array[lt];
                array[lt] = array[rt];
                array[rt] = tmp;

                lt++;
                rt++;
            }
        }

        return String.valueOf(array);
    }

    // 중복되는 문자 제거하기
    String removeDup(String str) {
        String answer = "";
        for (int i = 0; i < str.length(); i++) {
            if (str.indexOf(str.charAt(i)) == i) {
                answer += str.charAt(i);
            }
        }
        return answer;
    }

    // 팰린드롬
    String pal(String str) {
        // 1
        // String reversedStr = new StringBuilder(str).reverse().toString();
        // if (str.equalsIgnoreCase(reversedStr)) return "YES";
        // return "NO";

        // 2
        int len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - i - 1)) {
                return "NO";
            }
        }
        return "YES";
    }

    // 문자거리
    int[] distance(String str, char t) {
        int position = 1000;
        int[] ans = new int[str.length()];
        // 왼-> 오
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == t) {
                position = 0;
                ans[i] = position;
            } else {
                position++;
                ans[i] = position;
            }
        }
        // 오 -> 왼
        for (int i = str.length() - 1; i >= 0; i++) {
            if (str.charAt(i) == t) {
                position = 0;
            } else {
                position--;
                ans[i] = Math.min(ans[i], position);
            }
        }
        return ans;
    }

    // 문자열 압축
    String com(String str) {
        String ans = "";
        int cnt = 1;
        str = str + " ";

        for (int i = 0; i < str.length() - 1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                cnt += 1;
            } else {
                ans += str.charAt(i);
                if (cnt > 1)
                    ans += String.valueOf(cnt);
                cnt = 1;
            }
        }
        return ans;
    }

    // 암호화
    String encrypt(int n, String str) {
        String ans = "";
        for (int i = 0; i < n; i++) {
            String temp = str.substring(0, 7)
                    .replace("#", "1")
                    .replace("*", "0");

            int num = Integer.parseInt(temp);

            ans += (char) num;

            str = str.substring(7);
        }

        return ans;
    }
}
