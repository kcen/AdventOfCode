res = ARGF.read.split("\n\n").lazy.map do |v_group|
  v_group
    .split("\n")
    .map(&:to_i)
    .sum
end.sort[-3..]
puts [
  res[-1],
  res.sum,
]
