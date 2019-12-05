s,f=ARGF.read().strip.split('-')
p (s...f).each.select{|s|s==s.chars.sort.join}.select{|s|s.chars.uniq.map{|c|s.count(c)}.any?{|c|c==2}}.length
