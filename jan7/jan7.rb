def maximum_product(nums)
    nums.sort!
    len = nums.length
    product1 = nums[len - 1] * nums[len - 2] * nums[len - 3]
    product2 = nums[0] * nums[1] * nums[len - 1]
    [product1, product2].max
end

input = [1, 2, 3, 4]
result = maximum_product(input)
puts result