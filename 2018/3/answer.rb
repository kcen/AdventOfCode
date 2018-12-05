fabric = Hash.new{|h,k| h[k] = Array.new}
ARGF.map{ |line|
        l = line.scan(/\d+/).map(&:to_i)
        x = l[1].step.take(l[3])
        y = l[2].step.take(l[4])
        [l[0], x, y]
    }.each_with_object(fabric){ |(id,x,y),f|
        x.product(y).map{|p|f[p.to_s].push(id)}
    }.values.group_by{|v| v.length <=> 1}.tap{|x|
        #PART 1
        puts x[1].length
    }.transform_values(&:flatten).tap{|x|
        #PART2
        puts (x[0].uniq - x[1]).first
    }
