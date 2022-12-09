#!/bin/bash
export TIMEFORMAT=$'TIMING: real %3lR\n---------------------'
find . -mindepth 1 -type d | 
    sort | 
    xargs -I {} bash -c 'time echo -e "RESULT {}\n$(./{}/solve {}/input)"'
