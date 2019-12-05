s,f = ARGF.read().strip.split('-') #Args
p (s...f).each.
    select{|s|s==s.chars.sort.join}. #Sorted integers?
    select{|s|
        s.chars.uniq
            map{|c|s.count(c)}
            any?{|c|c==2}  #Doubles?
    }.length
