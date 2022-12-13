require "set"

priority = [nil, *"a".."z", *"A".."Z"].each_with_index.to_h

res = ARGF.readlines(chomp: true).map do |rucksack|
  s = rucksack.size / 2
  rucksack.chars
    .each_slice(s)
    .map(&:to_set)
    .inject(&:&)
    .first
end.map { |item| priority[item] }
puts res.sum
