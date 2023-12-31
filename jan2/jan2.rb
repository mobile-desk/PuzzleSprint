def is_palindrome(str)
    formatted_str = str.downcase.gsub(/[^a-zA-Z0-9]/, '')
    reversed_str = formatted_str.reverse
    formatted_str == reversed_str
end

input = "A man, a plan, a canal, Panama"
result = is_palindrome(input)
puts result
