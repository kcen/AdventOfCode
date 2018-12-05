require 'set'

puts ARGF.map(&:to_i).
        cycle.
        with_object(Set.new).
        inject{|(freq,*),(i,set)| break(freq) unless set.add?(freq); freq+i}
