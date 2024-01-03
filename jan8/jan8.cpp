#include <iostream>
#include <vector>
#include <cmath>

bool containsNearbyAlmostDuplicate(std::vector<int>& nums, int k, int t) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (std::abs((long long)nums[i] - nums[j]) <= t && std::abs(i - j) <= k) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    std::vector<int> nums = {1, 5, 9, 15, 20};
    int k = 3, t = 3;
    bool result = containsNearbyAlmostDuplicate(nums, k, t);
    std::cout << std::boolalpha << result << std::endl;
    return 0;
}