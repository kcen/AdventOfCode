def range_sorter(rng_1, rng_2)
  first = rng_1.first <=> rng_2.first
  if first == 0 # First digit matches
    # Reverse order last if first values match
    rng_2.last <=> rng_1.last
  else
    first
  end
end

# Part 1
cover_count = 0
# Part 2
overlap_count = 0

ARGF.readlines.map(&:strip).lazy.map do |line|
  # 33-62,26-62
  line.split(/[,-]/)
      .map(&:to_i)
      .each_slice(2)
      .map { |start, finish| start..finish }
      .sort{ |rng_1, rng_2| range_sorter(rng_1, rng_2) }
end.each do |elf_1, elf_2|
  cover_count += 1 if elf_1.cover?(elf_2)
  overlap_count += 1 if elf_1.include?(elf_2.first)
end

puts cover_count
puts overlap_count
