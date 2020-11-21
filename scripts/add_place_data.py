import requests
from bs4 import BeautifulSoup
import re 
import csv
# import ogr

# Now that I have the column of raw player data I need to extract the place data from it. 
# Essentially where is the player from, town/village/city, county, Province, Country, Provided all this data is available. 


rawName = csv.reader(open('raw/raw-player-data.csv','r'))
countyList = []

for row in rawName:
    counties = csv.reader(open('raw/irish-counties-list.csv','r'))
    if row[4] == "Raw-Birth-Data":
        print('no')
        continue

    else: 
        for county in counties:
            print(county[0])
            print(row[4])
                
            if county[0] in row[4]:
                print(county[0])
                countyList.append(county[0])
                
            else: 
                print('does not contain')
                
print(countyList) 

