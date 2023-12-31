def two_sum(nums, target)
    num_map = {}
    nums.each_with_index do |num, idx|
        complement = target - num
        return [num_map[complement], idx] if num_map[complement]
        num_map[num] = idx
    end
    []
end

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
puts result
