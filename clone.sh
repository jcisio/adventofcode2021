#!/bin/sh
cp -r day01 day$1
cd day$1
rename s/01/$1/ *.*
curl "https://adventofcode.com/2021/day/10/input" -H "cookie: session=$AOC2021SID" > d$1.in
echo -n > problem.md
git add d$1.in problem.md
