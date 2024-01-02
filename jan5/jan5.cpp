#include <iostream>
#include <vector>

void rearrangeEvenOdd(std::vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        if (nums[left] % 2 == 0) {
            left++;
        } else {
            std::swap(nums[left], nums[right]);
            right--;
        }
    }
}

int main() {
    std::vector<int> input = {3, 1, 2, 4, 6, 5, 7, 8};
    rearrangeEvenOdd(input);
    for (int num : input) {
        std::cout << num << " ";
    }
    return 0;
}