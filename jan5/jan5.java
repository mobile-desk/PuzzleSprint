public class RearrangeEvenOdd {
    public static void rearrangeEvenOdd(int[] nums) {
        int left = 0, right = nums.length - 1;
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

    public static void main(String[] args) {
        int[] input = {3, 1, 2, 4, 6, 5, 7, 8};
        rearrangeEvenOdd(input);
        for (int num : input) {
            System.out.print(num + " ");
        }
    }
}