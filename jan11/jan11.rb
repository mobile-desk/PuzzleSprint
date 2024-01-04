def reverse_words(s)
    s.split.reverse.join(' ')
end

input_str = "hello world"
result = reverse_words(input_str)
puts result