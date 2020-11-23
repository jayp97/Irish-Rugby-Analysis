import player_url_extractor as pue
import csv

# Data collected as of November 22 2020

playerList = csv.reader(open('raw/raw-player-data-country.csv','r')) 

with open('raw/player-career-data.csv', 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(["Player","Span","Matches","Starts","Subs","Points","Tries","Conversions","Penalties","Drop Goals","Won","Lost","Drawn"])

        for playerName in playerList: 

            # print(playerName[1])
            player = playerName[1]

            if player == "Player":
                continue

            else: 
                url = pue.PlayerURL(player).findURL()
                print(url)

                career = pue.PlayerCareerData(url).careerData()
                
                writer.writerow([player,career[0],career[1],career[2],career[3],career[4],career[5],career[6],career[7],career[8],career[9],career[10],career[11]])
