import requests
from bs4 import BeautifulSoup
import re 
import csv

# Now that I have the column of raw player data I need to extract the place data from it. 
# Essentially where is the player from, town/village/city, county, Province, Country, Provided all this data is available. 


rawName = csv.reader(open('raw/raw-player-data-towns.csv','r'))
# countyList = []

with open('raw/raw-player-data-counties.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Player", "Position", "Debut", "Raw-Birth-Data","BirthPlace", "County"])
    
    for row in rawName:

        counties = csv.reader(open('raw/irish-counties-list.csv','r'))
        riTowns = csv.reader(open('raw/irish-towns-list.csv','r')) 
        niTowns = csv.reader(open('raw/ni-towns-list.csv','r'))
        skip = False

        if row[4] == "Raw-Birth-Data":
            print('no')
            continue

        else: 
            for county in counties:
                print(county[0])
                print(row[4])
                    
                if county[0].lower() in row[4].lower():
                    print(county[0])
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],county[0]])
                    skip = True 

            if skip == False: 
                for ritown in riTowns: 

                    if ritown[0].lower() == row[5].lower(): 
                        print(ritown[0])
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],ritown[2]])
                        skip = True
            
            if skip == False: 
                for nitown in niTowns: 

                    if nitown[1].lower() == row[5].lower(): 
                        print(nitown[1])
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],nitown[4]])
                        skip = True

            if skip == False: 
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],"Unkown"])

            

                    
    # print(countyList) 

