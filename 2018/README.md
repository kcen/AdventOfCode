# 2018
We're golfing or something this year. Comments and tests are overrated, we'll ship directly to prod.

To run the code for every day, use this oneliner
```sh
$ for day in {1..25}; do echo "----DAY: ${day}---"; find ${day}/ -name '*.rb' -exec ruby {} ${day}/input \; ; done
```
or
```sh
$ cd 1/
$ ruby pt1.rb input
# Or with needles cat!
$ cat input | ruby pt2.rb
...etc
```
