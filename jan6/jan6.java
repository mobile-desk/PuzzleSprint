import java.util.LinkedHashMap;
import java.util.Map;

public class FirstNonRepeatingChar {
    public static char firstNonRepeatingChar(String s) {
        Map<Character, Integer> charMap = new LinkedHashMap<>();
        for (char c : s.toCharArray()) {
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }
        for (char c : s.toCharArray()) {
            if (charMap.get(c) == 1) {
                return c;
            }
        }
        return ' ';
    }

    public static void main(String[] args) {
        String input = "leetcode";
        char result = firstNonRepeatingChar(input);
        System.out.println(result);
    }
}