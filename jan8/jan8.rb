def contains_nearby_almost_duplicate(nums, k, t)
    n = nums.length
    (0...n).each do |i|
        ((i + 1)...n).each do |j|
            return true if (nums[i] - nums[j]).abs <= t && (i - j).abs <= k
        end
    end
    false
end

nums = [1, 5, 9, 15, 20]
k = 3
t = 3
result = contains_nearby_almost_duplicate(nums, k, t)
puts result