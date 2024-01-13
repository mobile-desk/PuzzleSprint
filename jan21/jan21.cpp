#include <iostream>

int countLegs(int chickens, int cows, int pigs) {
    int chickenLegs = chickens * 2;
    int cowLegs = cows * 4;
    int pigLegs = pigs * 4;

    return chickenLegs + cowLegs + pigLegs;
}

int main() {
    // Example usage
    int totalLegs = countLegs(2, 3, 5);
    std::cout << "Total number of legs: " << totalLegs << std::endl;

    return 0;
}