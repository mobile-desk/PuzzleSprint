def rearrange_even_odd(nums)
    left = 0
    right = nums.length - 1
    while left < right
        if nums[left].even?
            left += 1
        else
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        end
    end
end

input = [3, 1, 2, 4, 6, 5, 7, 8]
rearrange_even_odd(input)
puts input.join(" ")