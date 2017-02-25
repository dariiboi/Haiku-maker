import pickle
import sys
import random
import pprint
import operator
dict1 = pickle.load( open( "triChain.p", "rb" ) )
w1 = "$"
w2 = "#"
maxlines = 20
maxwords = 15
startWords = []
bigrams = list(dict1.keys())
for i in bigrams:
	if i[0] == '$':
		startWords.append(i[1])
def newTuple ():
	global startWords
	return ('$',random.choice(startWords))

#pprint.pprint (newTuple())
output = []
for i in range(maxlines):
	prevTuple = newTuple()
	j = 0
	output.append(prevTuple[1])
	while j < maxwords:
		j +=1
		newWord = max(dict1[prevTuple].items(), key=operator.itemgetter(1))[0]
		prevTuple = (prevTuple[1],newWord)
		output.append(newWord)
		if newWord == '#':		
			break
	output.pop()
	print(' '.join(output))
	output = []


