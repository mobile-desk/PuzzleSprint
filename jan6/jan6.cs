using System;
using System.Collections.Generic;

class Program {
    public static char FirstNonRepeatingChar(string s) {
        Dictionary<char, int> charMap = new Dictionary<char, int>();
        foreach (char c in s) {
            if (charMap.ContainsKey(c)) {
                charMap[c]++;
            } else {
                charMap[c] = 1;
            }
        }
        foreach (char c in s) {
            if (charMap[c] == 1) {
                return c;
            }
        }
        return ' ';
    }

    static void Main() {
        string input = "leetcode";
        char result = FirstNonRepeatingChar(input);
        Console.WriteLine(result);
    }
}