public class Palindrome {
    public static boolean isPalindrome(String str) {
        String formattedStr = str.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        String reversedStr = new StringBuilder(formattedStr).reverse().toString();
        return formattedStr.equals(reversedStr);
    }

    public static void main(String[] args) {
        String input = "A man, a plan, a canal, Panama";
        boolean result = isPalindrome(input);
        System.out.println(result);
    }
}
