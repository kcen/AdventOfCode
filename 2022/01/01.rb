res = ARGF.read.split("\n\n").lazy.map do |v_group|
  v_group
    .split("\n")
    .map(&:to_i)
    .sum
end
puts res.max
puts res.sort[-3..].sum
