import csv

playerData = csv.reader(open('data/player-data-country.csv','r'))
# countyList = []

with open('raw/player-data-debut.csv', 'w', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(["No.","Player","Debut"])
    
    for row in playerData:
        for date in range(1874, 2021): 
            if str(date) in row[3]: 
                writer.writerow([row[0],row[1],str(date)])
        
