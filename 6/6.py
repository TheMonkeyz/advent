#/usr/bin/python
import re
import Image

hrange = 1000
vrange = 1000

lights = [[False for x in range(hrange)] for x in range(vrange)]
litlights = 0
regex = re.compile('([a-z]* [a-z]*|[a-z]*) (\d*),(\d*) ([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)')


with open('input', 'r') as inf:
	for line in inf.readlines():
		match = regex.match(line)
		command = match.group(1)
		x1 = int(match.group(2))
		y1 = int(match.group(3))
		x2 = int(match.group(5))
		y2 = int(match.group(6))
		for x in range(x1,x2 + 1):
			for y in range(y1,y2 + 1):
				if command == 'turn on':
					lights[x][y] = True
#					print 'Turning on ' + str(x) + ',' + str(y)
				if command == 'turn off':
					lights[x][y] = False
#					print 'Turning off ' + str(x) + ',' + str(y)
				if command == 'toggle':
					if lights[x][y] == True:
						lights[x][y] = False
#						print 'Turning off ' + str(x) + ',' + str(y)
					else:
						lights[x][y] = True
#						print 'Turning on ' + str(x) + ',' + str(y)
inf.close()

img = Image.new( 'RGB', (hrange,vrange), 'black') 
pixels = img.load()

for x in range(hrange):
	for y in range(vrange):
		if lights[x][y] == True:
			pixels[x,y] = (255, 255, 255)
			litlights += 1		
print 'There are ' + str(litlights) + ' lights that are lit.'

img.show()
