#!/usr/bin/python

scale = 100 
gifted = 0
gifts = 0

location = [[0 for x in range(scale)] for x in range(scale)]

x = scale / 2
y = x

location[x][y] = 1

with open('input', 'r') as f:
	for char in f.read():
	#	print char
		if char == "^":
			y -= 1
		elif char == ">":
			x += 1
		elif char == "v":
			y += 1
		elif char == "<":
			x -= 1
		location[x][y] += 1
f.closed

for y in range(scale):
	for x in range(scale):
	#	print 'x: ' + str(x) + 'y: ' + str(y)
		if location[x][y] > 0:
			gifted += 1
			gifts += location[x][y]

print 'Gifted: ' + str(gifted)
print 'Gifts: ' + str(gifts)
