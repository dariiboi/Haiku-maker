from __future__ import division
import string 
import pickle
from bs4 import BeautifulSoup
import csv
import re
import os
import sys
import random
import pprint

sys.getdefaultencoding()
badcount = 0
path = '/Users/darius/Documents/ComSci2/project4/lyricsmode'
dict1 = {}
words = []
wordCount = 0.0

def generate_trigram(words):
    if len(words) < 3:
        return
    for i in range(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])
 
 #count the words
def count(line):
	global dict1
	global wordCount
	words = line.split(' ')
	wordCount += len(words)
	for word1, word2, word3 in generate_trigram(words):
		key = (word1, word2)
		if key in dict1:
			if word3 in dict1[key]:
				dict1[key][word3] += 1.0
			else:
				dict1[key][word3] = 1.0
		else:
			dict1[key] = {}
			dict1[key][word3] = 1.0
		


for filename in os.listdir(path):
	#filename = filename.decode('utf8')
	myfile = path+"/"+filename
	#print(myfile)
	pretext = ''
	t= ''
	t2= u''	
	try:
		f = open(myfile, 'rb')
		t2 = f.read().decode('utf8', 'ignore')
		#t2 = open(myfile, encoding="utf-8").read()
	except:
		t2 = open(myfile, encoding="latin-1 ").read()
		print("fallback to latin 1:", sys.exc_info()[1])
		e = sys.exc_info()[0]
		print("latin file: \n"+ myfile)
	try:
		soup = BeautifulSoup(t2, "html.parser")
		#soup = BeautifulSoup.BeautifulSoup(content.decode('utf-8','ignore'))
		pretext = soup.find_all('pre')
	except: 
		badcount+=1
		#if all other checks fail, go here
		print("Unexpected error from soup:", sys.exc_info()[1])
	
	if len(pretext) > 0:
		for t in pretext:
			t = t.get_text()
	else:
		try:
			rawfile = open(myfile, encoding='latin1')
			t = rawfile.read()
		except:
			print("badfile2 :"+ myfile)
	t = t.lower()
	t = re.sub("[\(\[].*?[\)\]]", "", t)
	t = re.sub("[^a-z0-9' \n]*", "", t)

	#print(t)
	lines = t.split('\n')
	lines = lines[6:]
	for line in lines:
		line = ' '.join(line.split())
		if re.match('\w+',line):
			newline = '$ ' + line + ' #'
			count(newline)
for key in dict1:
	for word in dict1[key]:
		dict1[key][word] = dict1[key][word]/wordCount

pprint.pprint(dict1)		
pickle.dump( dict1, open( "triChain.p", "wb" ) )	
# GENERATE OUTPUT

