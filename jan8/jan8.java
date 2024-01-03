public class ContainsNearbyAlmostDuplicate {
    public static boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Math.abs((long) nums[i] - nums[j]) <= t && Math.abs(i - j) <= k) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {1, 5, 9, 15, 20};
        int k = 3, t = 3;
        boolean result = containsNearbyAlmostDuplicate(nums, k, t);
        System.out.println(result);
    }
}