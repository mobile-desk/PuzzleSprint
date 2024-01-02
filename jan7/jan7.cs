using System;
using System.Linq;

class Program {
    public static int MaximumProduct(int[] nums) {
        Array.Sort(nums);
        int len = nums.Length;
        int product1 = nums[len - 1] * nums[len - 2] * nums[len - 3];
        int product2 = nums[0] * nums[1] * nums[len - 1];
        return Math.Max(product1, product2);
    }

    static void Main() {
        int[] input = {1, 2, 3, 4};
        int result = MaximumProduct(input);
        Console.WriteLine(result);
    }
}