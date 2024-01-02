#include <iostream>
#include <unordered_map>

char firstNonRepeatingChar(std::string s) {
    std::unordered_map<char, int> charMap;
    for (char c : s) {
        charMap[c]++;
    }
    for (char c : s) {
        if (charMap[c] == 1) {
            return c;
        }
    }
    return ' ';
}

int main() {
    std::string input = "leetcode";
    char result = firstNonRepeatingChar(input);
    std::cout << result << std::endl;
    return 0;
}