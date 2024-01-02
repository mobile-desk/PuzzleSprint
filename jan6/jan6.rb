def first_non_repeating_char(s)
    char_count = Hash.new(0)
    s.each_char { |c| char_count[c] += 1 }
    s.each_char { |c| return c if char_count[c] == 1 }
    ' '
end

input = "leetcode"
result = first_non_repeating_char(input)
puts result