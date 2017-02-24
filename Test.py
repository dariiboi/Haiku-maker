from __future__ import division
import string 
import pickle
from bs4 import BeautifulSoup
import csv
import re
import os
import sys

sys.getdefaultencoding()
badcount = 0
path = '/Users/darius/Documents/ComSci2/project4/lyricsmode'
dict1 = {}
words = []
dict2 = {}
wordCount = 0.0
#count the words
def count(line):
	global dict1
	global dict2
	global wordCount
	words = line.split(' ')
	for i in words:
		wordCount +=1.0
	
	for i in range(2,len(words)):
		if words[i] in dict1:
			if words[i-1] in dict1[words[i]]:
				dict1[words[i]][words[i-1]] += 1.0	
			else:
				dict1[words[i]][words[i-1]] = 1.0
			#Turn word count into probability by dividing it by the total number of words
			dict1[words[i]][words[i-1]] = dict1[words[i]][words[i-1]] / wordCount
		else:
			dict1[words[i]]={}
		#look 2 words back and add that to dictionary 2	
		if words[i] in dict2:
			if words[i-2] in dict2[words[i]]:
				dict2[words[i]][words[i-2]] += 1.0	
			else:
				dict2[words[i]][words[i-2]] = 1.0
			#Turn word count into probability by dividing it by the total number of words
			dict2[words[i]][words[i-2]] = dict2[words[i]][words[i-2]] / wordCount
		else:
			dict2[words[i]]={}
	#pickle.dump( dict1, open( "save.p", "wb" ) )	
	#pickle.dump( dict2, open( "save2.p", "wb" ) )

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
print(dict1['fuck'])


