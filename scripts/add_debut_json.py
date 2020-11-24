import json 
import csv

playerCareer = csv.reader(open('raw/player-data-debut.csv','r'))

with open('data/player-data-career.json') as f:
  playerData = json.load(f)

i = 1
for row in playerCareer: 

    # dict_name.update({'item': 3})
    if row[1] == "Player": 
        continue

    else: 
        playerData[str(i)]["debut year"] = row[2]

        if i < 1120: 
            i=i+1 


with open("data/player-data-debut.json", "w") as write_file:
    json.dump(playerData, write_file)
