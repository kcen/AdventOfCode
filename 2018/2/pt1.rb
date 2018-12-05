puts ARGF.map{ |line|
            line.
                each_char.
                with_object(Hash.new(0)){|c,h| h[c]+=1}.
                invert.
                values_at(2,3)
        }.
        transpose.
        map(&:compact).
        map(&:length).
        inject(&:*)
