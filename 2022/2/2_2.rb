def points(them, me)
    case me
    when "X" # Lose
        0 + case them
        when "A" # Elf rock
            3 # Scissors
        when "B" # Elf paper
            1 # Rock
        else # Elf scissors
            2 # Paper
        end
    when "Y" # Draw
        3 + {
            "A" => 1, #Rock
            "B" => 2, #Paper
            "C" => 3, #Scissors
        }[them]
    when "Z" # Win
        6 + case them
        when "A" # Elf rock
            2 # Paper
        when "B" # Elf paper
            3 # Scissors
        else # Elf scissors
            1 # Rock
        end
    end
end

res = ARGF.readlines.map(&:split).
    map{|them, me| points(them, me)}

puts res.sum