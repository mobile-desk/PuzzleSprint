using System;
using System.Linq;
using System.Text.RegularExpressions;

class Program {
    public static bool IsPalindrome(string str) {
        string formattedStr = Regex.Replace(str.ToLower(), @"[^a-zA-Z0-9]", "");
        string reversedStr = new string(formattedStr.Reverse().ToArray());
        return formattedStr == reversedStr;
    }

    static void Main() {
        string input = "A man, a plan, a canal, Panama";
        bool result = IsPalindrome(input);
        Console.WriteLine(result);
    }
}
