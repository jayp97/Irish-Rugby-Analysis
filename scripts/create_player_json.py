import json 
import csv 

playerList = csv.reader(open('data/player-data-country.csv','r'))
playerDebut = csv.reader(open('raw/player-data-debut.csv','r'))

playerData = {}

for row in playerList: 

    # dict_name.update({'item': 3})
    if row[1] == "Player": 
        continue
    
    else: 
        index = int(row[0])
        playerData[index] = {
            "id": row[0],
            "name": row[1],
            "position": row[2],
            "debut year": None, 
            "birth place":{
                "place": row[5],
                "county": row[6],
                "province": row[7],
                "country": row[8]
            },
            "statistics":{
                "career span": None,
                "matches": None,
                "starts": None,
                "substitutions": None,
                "points": None,
                "tries": None,
                "conversions": None,
                "penalties": None,
                "drop goals": None,
                "GfM": None,
                "won": None,
                "lost": None,
                "drawn": None
            }
        }

with open("data/player-data.json", "w") as write_file:
    json.dump(playerData, write_file)