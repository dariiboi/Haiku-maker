import pickle
from bs4 import BeautifulSoup
import csv
import re
import os
import sys
sys.getdefaultencoding()
badcount = 0
path = '/Users/darius/Documents/ComSci2/project4/lyricsmode'
for filename in os.listdir(path):
	#filename = filename.decode('utf8')
	myfile = path+"/"+filename
	#print(myfile)
	pretext = ''
	t= ''
	t2= u''	
	try:
		t2 = open(myfile, encoding="utf-8").read()
	except:
		t2 = open(myfile, encoding="latin-1").read()
		print("fallback to latin 1:", sys.exc_info()[1])
		#e = sys.exc_info()[0]
		print("latin file: \n"+ myfile)
	try:
		soup = BeautifulSoup(t2, "html.parser")
		#soup = BeautifulSoup.BeautifulSoup(content.decode('utf-8','ignore'))
		pretext = soup.find_all('pre')
	except: 
		badcount+=1
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
		if re.match('\w+',line):
			newline = '$ ' + line + ' #'
			#print(newline)
print(badcount)