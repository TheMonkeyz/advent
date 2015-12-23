#!/usr/bin/python

import hashlib

for i in range (999999):

	hash = hashlib.md5("ckczppom" + str(i)).hexdigest()
#	print str(i) + ': ' + hash 
	stripped = str(hash[:5])
	print str(i) + ':' + stripped
	if stripped == "00000":
		print "Answer is: " + str(i)
		break

