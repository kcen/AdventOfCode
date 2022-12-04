# {
#     "A" => 1, #Rock
#     "B" => 2, #Paper
#     "C" => 3, #Scissors
# }

def points(them, me)
  case me
  when 'X' # Lose
    0 + {
      'A' => 3, # Scissors
      'B' => 1, # Rock
      'C' => 2 # Papper
    }[them]
  when 'Y' # Draw
    3 + {
      'A' => 1, # Rock
      'B' => 2, # Paper
      'C' => 3 # Scissors
    }[them]
  when 'Z' # Win
    6 + {
      'A' => 2, # Paper
      'B' => 3, # Scissors
      'C' => 1 # Rock
    }[them]
  end
end

res = ARGF.readlines.map(&:split).lazy.map { |them, me| points(them, me) }

puts res.sum
