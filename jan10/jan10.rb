def search_insert(nums, target)
    left = 0
    right = nums.length

    while left < right
        mid = left + (right - left) / 2
        if nums[mid] == target
            return mid
        elsif nums[mid] < target
            left = mid + 1
        else
            right = mid
        end
    end

    left
end

nums = [1, 3, 5, 6]
target1 = 5
target2 = 2

puts search_insert(nums, target1) # Output: 2
puts search_insert(nums, target2) # Output: 1