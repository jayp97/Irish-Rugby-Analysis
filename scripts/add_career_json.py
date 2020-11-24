import json 
import csv

playerCareer = csv.reader(open('data/player-career-data.csv','r'))

with open('data/player-data.json') as f:
  playerData = json.load(f)

i = 1
for row in playerCareer: 

    # dict_name.update({'item': 3})
    if row[1] == "Player": 
        continue

    else: 
        playerData[str(i)]["statistics"] = {
                "career span": row[2],
                "matches": row[3],
                "starts": row[4],
                "substitutions": row[5],
                "points": row[6],
                "tries": row[7],
                "conversions": row[8],
                "penalties": row[9],
                "drop goals": row[10],
                "GfM": row[11],
                "won": row[12],
                "lost": row[13],
                "drawn": row[14]
            }

        if i < 1120: 
            i=i+1 


with open("data/player-data-career.json", "w") as write_file:
    json.dump(playerData, write_file)


        # index = int(row[0])
        # playerData[index] = {
        #     "id": row[0],
        #     "name": row[1],
        #     "position": row[2],
        #     "debut year": None, 
        #     "birth place":{
        #         "place": row[5],
        #         "county": row[6],
        #         "province": row[7],
        #         "country": row[8]
        #     },
        #     "statistics":{
        #         "career span": None,
        #         "matches": None,
        #         "starts": None,
        #         "substitutions": None,
        #         "points": None,
        #         "tries": None,
        #         "conversions": None,
        #         "penalties": None,
        #         "drop goals": None,
        #         "won": None,
        #         "lost": None,
        #         "drawn": None
        #     }
        # }