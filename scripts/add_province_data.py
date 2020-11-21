import requests
from bs4 import BeautifulSoup
import re 
import csv

# I just have to check each of the county cells and see if it contains something other than Unknown. if so I check the content against my irish counties list and return the province. 

rawName = csv.reader(open('raw/raw-player-data-counties.csv','r'))
# countyList = []

with open('raw/raw-player-data-province.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Player", "Position", "Debut", "Raw-Birth-Data","BirthPlace","County","Province"])
    skip = False 
    
    for row in rawName:
        counties = csv.reader(open('raw/irish-counties-list.csv','r'))

        if row[6] == "County":
            print('no')

        elif row[6] == "Unkown": 
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],"Uknown"])

        else: 
            for county in counties:

                if county[0].lower() == row[6].lower():
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],county[1]])




                

