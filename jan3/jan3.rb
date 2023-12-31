def judge_circle(moves)
    x = 0
    y = 0
    moves.each_char do |move|
        case move
        when 'U'
            y += 1
        when 'D'
            y -= 1
        when 'L'
            x -= 1
        when 'R'
            x += 1
        end
    end
    x.zero? && y.zero?
end

input = "UD"
result = judge_circle(input)
puts result
