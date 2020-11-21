import requests
from bs4 import BeautifulSoup
import re 
import csv

rawName = csv.reader(open('raw/raw-player-data-province.csv','r'))

duplicates =[]
current = str()

for row in rawName:

    if row[0] == "No.":
        continue

    elif row[0] == current: 
        duplicates.append(row[0])
        current = row[0]
    
    else: 
        current = row[0]


print(duplicates)