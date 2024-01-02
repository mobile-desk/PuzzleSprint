import java.util.Arrays;

public class MaximumProduct {
    public static int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int len = nums.length;
        int product1 = nums[len - 1] * nums[len - 2] * nums[len - 3];
        int product2 = nums[0] * nums[1] * nums[len - 1];
        return Math.max(product1, product2);
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3, 4};
        int result = maximumProduct(input);
        System.out.println(result);
    }
}