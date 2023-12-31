#include <iostream>

bool judgeCircle(std::string moves) {
    int x = 0, y = 0;
    for (char move : moves) {
        if (move == 'U') y++;
        else if (move == 'D') y--;
        else if (move == 'L') x--;
        else if (move == 'R') x++;
    }
    return x == 0 && y == 0;
}

int main() {
    std::string input = "UD";
    bool result = judgeCircle(input);
    std::cout << std::boolalpha << result << std::endl;
    return 0;
}
