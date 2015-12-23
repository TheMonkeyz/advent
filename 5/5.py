#!/usr/bin/python
import re
nicestrings = 0
with open('input', 'r') as inf:
	for line in inf.readlines():
		vowels = 0
		for letter in line:
			if re.search(r'a|e|i|o|u', letter):
				vowels += 1
		if vowels > 2:
			if re.search(r'(\w)\1+', line):
				if not re.search(r'ab|cd|pq|xy', line):
					nicestrings += 1
inf.close()
print 'There are ' + str(nicestrings) + ' nice strings.'

			
