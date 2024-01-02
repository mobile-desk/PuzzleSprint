#include <iostream>
#include <vector>
#include <algorithm>

int maximumProduct(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int len = nums.size();
    int product1 = nums[len - 1] * nums[len - 2] * nums[len - 3];
    int product2 = nums[0] * nums[1] * nums[len - 1];
    return std::max(product1, product2);
}

int main() {
    std::vector<int> input = {1, 2, 3, 4};
    int result = maximumProduct(input);
    std::cout << result << std::endl;
    return 0;
}