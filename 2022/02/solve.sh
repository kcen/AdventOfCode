#!/usr/bin/env bash
base_dir=$(dirname $(realpath $0))
[ -z "$AOC_INPUT" ] && AOC_INPUT=$base_dir/input
ruby $base_dir/02_1.rb $AOC_INPUT
ruby $base_dir/02_2.rb $AOC_INPUT