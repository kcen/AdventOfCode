SCORE = {
  "A" => 1,
  "X" => 1,
  "B" => 2,
  "Y" => 2,
  "C" => 3,
  "Z" => 3,
}

def points(them, me)
  s_t = SCORE[them]
  s_me = SCORE[me]
  case (s_me - s_t) % 3
  when 0 # Draw
    3
  when 1 # Win
    6
  else # Lose
    0
  end + s_me
end

res = ARGF.readlines.map(&:split).lazy.map { |them, me| points(them, me) }

puts res.sum
