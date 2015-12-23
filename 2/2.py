#!/usr/bin/python

with open('input.txt', 'r') as inf:
	size = 0
	for line in inf:
		line = line.rstrip().split("x")
		l = int(line[0])
		w = int(line[1])
		h = int(line[2])
		s1 = l * w
		s2 = w * h
		s3 = h * l
		box = 2 * s1 + 2 * s2 + 2 * s3
		extra = min(s1, s2, s3)
		size = box + extra + size
		print size
