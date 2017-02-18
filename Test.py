import pickle
from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("/Users/darius/Documents/ComSci2/project4/lyricsmode/backseat.ken.txt"), "html.parser")

print(soup.get_text())