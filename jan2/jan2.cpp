#include <iostream>
#include <cctype>
#include <algorithm>

bool isPalindrome(std::string str) {
    str.erase(std::remove_if(str.begin(), str.end(), [](char c) {
        return !std::isalnum(c);
    }), str.end());
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);
    std::string reversedStr = str;
    std::reverse(reversedStr.begin(), reversedStr.end());
    return str == reversedStr;
}

int main() {
    std::string input = "A man, a plan, a canal, Panama";
    bool result = isPalindrome(input);
    std::cout << std::boolalpha << result << std::endl;
    return 0;
}
