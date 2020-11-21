import requests
from bs4 import BeautifulSoup
import re 
import csv
# import ogr

# Now that I have the column of raw player data I need to extract the place data from it. 
# Essentially where is the player from, town/village/city, county, Province, Country, Provided all this data is available. 


rawName = csv.reader(open('raw/raw-player-data.csv','r'))
# townList = []


with open('raw/raw-player-data-towns.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Player", "Position", "Debut", "Raw-Birth-Data","BirthPlace"])

    for row in rawName:
        riTowns = csv.reader(open('raw/irish-towns-list.csv','r'))
        skip = False 
        

        if row[4] == "Raw-Birth-Data":
            print('no')
            continue

        else:
            for ritown in riTowns:
                niTowns = csv.reader(open('raw/ni-towns-list.csv','r'))
                
                # print(ritown[0])
                # print(row[4])
                    
                if ritown[0].lower() in row[4].lower():
                    print(ritown[0])
                    # townList.append(ritown[0])
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],ritown[0]])
                    skip = True 
                    # continue

                elif ritown[0].lower() == "youghal" and ritown[0].lower() not in row[4].lower():
                    

                    for nitown in niTowns:
                        print(nitown[1])
                    # print(row[4])
                        
                        if nitown[1].lower() in row[4].lower():
                            print(nitown[1])
                            # townList.append(nitown[1])
                            writer.writerow([row[0],row[1],row[2],row[3],row[4],nitown[1]])
                            skip = True 
                            continue 

                        # elif nitown[1].lower() == "bryansford" and nitown[1].lower() not in row[4].lower():
                        #     writer.writerow([row[0],row[1],row[2],row[3],row[4],"Unknown"])
                        #     continue

                        else: 
                            print('does not contain nitown')

                    if skip == False:
                        writer.writerow([row[0],row[1],row[2],row[3],row[4],"Unknown"])

                else: 
                    print('does not contain ritown')
                    


               


                            

                
# print(townList) 