function containsNearbyAlmostDuplicate(nums, k, t) {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (Math.abs(nums[i] - nums[j]) <= t && Math.abs(i - j) <= k) {
                return true;
            }
        }
    }
    return false;
}

const nums = [1, 5, 9, 15, 20];
const k = 3;
const t = 3;
const result = containsNearbyAlmostDuplicate(nums, k, t);
console.log(result);