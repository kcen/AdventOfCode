res = ARGF.read.split("\n\n").map{|v_group|
    v_group.
      split("\n").
      map(&:to_i).
      sum
  }

puts res.max