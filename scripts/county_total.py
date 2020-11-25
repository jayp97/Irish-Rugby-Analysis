import json 
import analysis 
import csv

countyList = csv.reader(open('raw/irish-counties-list.csv','r'))

with open('data/total-players-per-county.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["County","Total Players"])
  

    for county in countyList:

        if county[1] == 'province':
            pass

        else: 
            countyTotal = analysis.PlayersPerCounty(county[0]).ppCounty()
            writer.writerow([county[0],countyTotal])




