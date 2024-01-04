public class ReverseWords {
    public static String reverseWords(String s) {
        String[] words = s.split("\\s+");
        StringBuilder reversed = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            reversed.append(words[i]);
            if (i != 0) {
                reversed.append(" ");
            }
        }

        return reversed.toString();
    }

    public static void main(String[] args) {
        String input = "hello world";
        String result = reverseWords(input);
        System.out.println(result);
    }
}