from os import *
from sys import *
from collections import *
from math import *

# main catch is to sort by unit weight values and pick once at a time
def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	items.sort(key=lambda x:x[1]/x[0], reverse=True)

	finalValue = 0
	remainingWeight = w
	for wt,value in items:
		if wt < remainingWeight:
			finalValue += value
		else:
			finalValue += (value/wt)*remainingWeight
			break
		remainingWeight -= wt
	return finalValue