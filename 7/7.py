#!/usr/bin/python
import re

firstinputpattern = re.compile('([0-9]*) -> ([a-z]*)')
inputpattern = re.compile('([a-z*) -> ([a-z]*)')
notpattern = re.compile(r'NOT ([a-z]*|[0-9]*) -> ([a-z]*)')
otherspattern = re.compile(r'([a-z]*|[0-9]*) ([A-Z]*) ([a-z]*|[0-9]*) -> ([a-z]*)')
WandS = {}

def is_number(s):
	try:
        	int(s)
	        return True
	except ValueError:
        	return False

with open('input', 'r') as inf:
	for line in inf.readlines():
		if re.match(r'[0-9]* ->', line):
			print line
			match = firstinputpattern.match(line)
			source = int(match.group(1))
			dest = match.group(2)
			WandS[dest] = source
inf.close()
found = False
while found == False:
	with open('input', 'r') as inf:
		for line in inf.readlines():
#			print line
			if re.match(r'NOT', line):
				match = notpattern.match(line)
				source = match.group(1)
				dest = match.group(2)
				if is_number(source):
					WandS[dest] = ~ source
				else:
					if WandS.get(source):
						WandS[dest] = ~ WandS[source]

			elif re.match(r'[a-z]* > [a-z]*', line):
				source = match.group(1)	
				dest = match.group(2)
				if WandS.get(source):
					WandS[dest] = WandS[source]

			elif re.match(r'([a-z]*|[0-9]*) ([A-Z]*) ([a-z]*|[0-9]*) -> ([a-z]*)', line):
				match = otherspattern.match(line)
				source = match.group(1)
				operand = match.group(2)
				mod = match.group(3)
				dest = match.group(4)
				srcIsSet = False
				modIsSet = False

				if not is_number(source):
					if WandS.get(source):
						srcIsSet = True
						source = int(WandS[source])
				else:
					srcIsSet = True

				if not is_number(mod):
					if WandS.get(mod):
						modIsSet = True
						mod = int(WandS[mod])
				else:
						modIsSet = True
				
				if srcIsSet and modIsSet:
					source = int(source)
					mod = int(mod)
					if operand == 'AND':
						WandS[dest] = source & mod

					if operand == 'LSHIFT':				
						WandS[dest] = source << mod

					if operand == 'RSHIFT':				
						WandS[dest] = source >> mod

					if operand == 'OR':				
						WandS[dest] = source ^ mod
		print WandS
		try:
			print a
		except:
			found = False
	inf.close()
