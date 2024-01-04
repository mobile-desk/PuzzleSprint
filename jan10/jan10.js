function searchInsert(nums, target) {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

const nums = [1, 3, 5, 6];
const target1 = 5;
const target2 = 2;

console.log(searchInsert(nums, target1)); // Output: 2
console.log(searchInsert(nums, target2)); // Output: 1