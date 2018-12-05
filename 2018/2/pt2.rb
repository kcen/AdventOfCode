puts ARGF.map(&:chars).combination(2).
        map{|a,b| a.zip(b).select{|x,y| x == y }.map(&:first)}.
        max_by(&:length).join
