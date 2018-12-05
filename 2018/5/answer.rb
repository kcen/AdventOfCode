i = ARGF.first.chomp #Input
r = Regexp.new((('a'..'z').zip('A'..'Z')).map{|a,b|a+b+'|'+b+a}.join('|')) #Regex
1.step.find{!i.gsub!(r,'')} #Magic

#Part 1
puts i.length

#Part 2
puts ('a'..'z').map{|c| i.gsub(/#{c}/i,'')}.
        map{|x| 1.step.find{ !x.gsub!(r,'')}; x.length}.min
