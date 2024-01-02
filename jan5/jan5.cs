using System;

class Program {
    public static void RearrangeEvenOdd(int[] nums) {
        int left = 0, right = nums.Length - 1;
        while (left < right) {
            if (nums[left] % 2 == 0) {
                left++;
            } else {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                right--;
            }
        }
    }

    static void Main() {
        int[] input = {3, 1, 2, 4, 6, 5, 7, 8};
        RearrangeEvenOdd(input);
        foreach (int num in input) {
            Console.Write(num + " ");
        }
    }
}