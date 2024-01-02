function maximumProduct(nums) {
    nums.sort((a, b) => a - b);
    const len = nums.length;
    const product1 = nums[len - 1] * nums[len - 2] * nums[len - 3];
    const product2 = nums[0] * nums[1] * nums[len - 1];
    return Math.max(product1, product2);
}

const input = [1, 2, 3, 4];
const result = maximumProduct(input);
console.log(result);