function rearrangeEvenOdd(nums) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        if (nums[left] % 2 === 0) {
            left++;
        } else {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            right--;
        }
    }
    return nums;
}

const input = [3, 1, 2, 4, 6, 5, 7, 8];
rearrangeEvenOdd(input);
console.log(input);