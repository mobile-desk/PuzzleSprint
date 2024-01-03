using System;

class Program {
    public static bool ContainsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Math.Abs((long)nums[i] - nums[j]) <= t && Math.Abs(i - j) <= k) {
                    return true;
                }
            }
        }
        return false;
    }

    static void Main() {
        int[] nums = {1, 5, 9, 15, 20};
        int k = 3, t = 3;
        bool result = ContainsNearbyAlmostDuplicate(nums, k, t);
        Console.WriteLine(result);
    }
}