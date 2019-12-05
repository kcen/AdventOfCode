

input = ARGF.to_a


def dist(p1,p2)
    p1.zip(p2).map{|xy1, xy2| (xy1-xy2).abs}.inject(&:+)
end

coords = input.map{|i| i.scan(/\d+/).map(&:to_i)}

puts coords.inspect

grid_size = coords.transpose.map(&:minmax)

puts grid_size.inspect

grid_points = grid_size.map{|x| Range.new(*x).to_a}.inject(&:product)

closest_points = grid_points.map{|p| coords.min_by(2){|x| dist(p,x)} }



require 'pry'
binding.pry
