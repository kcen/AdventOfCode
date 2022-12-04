require 'set'

priority = [nil, *'a'..'z', *'A'..'Z']

res = ARGF.readlines.map(&:strip).each_slice(3)
          .map do |group|
            group.map do |rucksack|
            rucksack.chars.to_set
          end.inject(&:&).first
      end.map do |duplicate_item|
        priority.index(duplicate_item)
      end

puts res.sum
