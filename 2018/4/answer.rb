oncall_elf = nil
sleep_shifts = Hash.new{|h,k| h[k] = Array.new }
sleep_minute = nil
ARGF.sort.each do |line|
    new_guard = line[/(?<=Guard #)\d+/]
    if new_guard
        oncall_elf = new_guard.to_i
    else
        minute = line[/(?<=00:)\d\d\]/].to_i
        if line[/falls asleep/]
            sleep_minute = minute
        else
            sleep_shifts[oncall_elf] += [sleep_minute...minute]
        end
    end
end

sleeps_by_minute = {}

sleep_shifts.each do |elf, sleeps|
    sleeps_by_minute[elf] = 60.times.map do |minute|
        sleeps.map{|r| r.include?(minute)}.count(true)
    end
end

#PART1
elf, minutes = sleeps_by_minute.max_by{|elf, minutes| minutes.sum}
most_minutes = minutes.index(minutes.max)
puts elf * most_minutes

#PART2
elf, minutes = sleeps_by_minute.max_by{|elf, minutes| minutes.max}
max_minute = minutes.index(minutes.max)
puts elf * max_minute
