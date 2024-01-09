def generate_multiplication_table(number, range_limit)
    puts "Multiplication table for #{number} up to #{number} * #{range_limit}:\n"
    (1..range_limit).each do |i|
        puts "#{number} * #{i} = #{number * i}"
    end
end

def main()
    print "Enter a number: "
    number = gets.chomp.to_i
    print "Enter the range: "
    range_limit = gets.chomp.to_i

    generate_multiplication_table(number, range_limit)
end

main()