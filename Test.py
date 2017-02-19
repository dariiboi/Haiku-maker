import pickle
from bs4 import BeautifulSoup
import csv
import re
import os
import sys
path = '/Users/darius/Documents/ComSci2/project4/lyricsmode'
for filename in os.listdir(path):
	myfile = path+"/"+filename
	#print(myfile)
	pretext = ''
	t= ''
	try:
		soup = BeautifulSoup(open(myfile), "html.parser")
		#soup = BeautifulSoup.BeautifulSoup(content.decode('utf-8','ignore'))
		pretext = soup.find_all('pre')
	except:
		#print("Unexpected error:", sys.exc_info()[0])
		#e = sys.exc_info()[0]
		print("badfile: \n"+ myfile)
	
	if len(pretext) > 0:
		for t in pretext:
			t = t.get_text()
	else:
		try:
			rawfile = open(myfile)
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