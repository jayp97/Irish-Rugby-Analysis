import requests
from bs4 import BeautifulSoup
import re 
import csv

# check province against the county list and return the country (republic of ireland or Norhtern Ireland). If nothing found see if the raw player birth data countains a foreign country by running it against the countries list and checking for membership. 

rawName = csv.reader(open('raw/raw-player-data-province.csv','r'))
# countyList = []

# with open('raw/raw-player-data-country.csv', 'w', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(["No.", "Player", "Position", "Debut", "Raw-Birth-Data","BirthPlace","County","Province","Country"])
    
    
    for row in rawName:
        counties = csv.reader(open('raw/irish-counties-list.csv','r'))
        countries = csv.reader(open('raw/countries-of-world.csv','r'))
        skip = False 

        if row[7] == "Province":
            print('no')

        elif row[7] == "Unknown":
            for country in countries:
            
                if country[1].lower() in row[4].lower():
                    print(country[1])
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],country[1]])
                    skip = True 
                
            if skip == False: 
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],"Unknown"])
                skip = True

        
        else: 
            for county in counties: 
                if county[0].lower() == row[6].lower(): 
                    print(county[1])
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],county[2]])
                    skip = True

            if skip == False: 
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],"Unknown"])
                skip = True
