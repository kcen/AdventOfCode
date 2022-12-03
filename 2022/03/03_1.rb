require 'set'

priority = [nil, *'a'..'z', *'A'..'Z']

res = ARGF.readlines.map(&:strip)
    .map do |rucksack|
        s = rucksack.size/2
        rucksack.chars
            .each_slice(s)
            .map(&:to_set)
            .inject(&:&)
            .first
    end.map do |duplicate_item|
        priority.index(duplicate_item)
    end
puts res.sum