SCORE = {
  'A' => 1,
  'X' => 1,
  'B' => 2,
  'Y' => 2,
  'C' => 3,
  'Z' => 3
}

def points(them, me)
  s_t = SCORE[them]
  s_me = SCORE[me]
  if s_t == s_me
    3 + s_me # Draw
  elsif s_me == 1 && s_t == 2
    s_me
  elsif s_me == 2 && s_t == 3
    s_me
  elsif s_me == 3 && s_t == 1
    s_me
  else
    s_me + 6
  end
end

res = ARGF.readlines.map(&:split)
          .map { |them, me| points(them, me) }

puts res.sum
