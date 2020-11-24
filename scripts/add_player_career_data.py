import player_url_extractor as pue
import csv

# Data collected as of November 24 2020

playerList = csv.reader(open('data/player-data-country.csv','r')) 

numbers = [229, 832, 440, 841, 657, 15, 331, 1088, 731, 231, 825, 114, 656, 597, 1095, 517, 810, 481, 171, 253, 924, 883, 620, 402, 93, 116, 809, 735, 241, 542]

with open('raw/player-career-data.csv', 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(["ID","Player","Span","Matches","Starts","Subs","Points","Tries","Conversions","Penalties","Drop Goals","GfM","Won","Lost","Drawn"])

        for playerName in playerList: 

            # print(playerName[1])
            player = playerName[1]

            if player == "Player":
                continue


            if int(playerName[0]) in range(1,784): 

                if int(playerName[0]) in numbers:
                    url = pue.PlayerURL(player).findURL()
                    # print(url)
                    print(playerName[0])

                    career = pue.PlayerCareerData(url).careerData()
                    
                    writer.writerow([playerName[0],player,career[0],career[1],career[2],career[3],career[4],career[5],career[6],career[7],career[8],"Null",career[9],career[10],career[11]])

                # I need to fix this manually as Robert Morrow occurs twice. The first instance of this player is incorrect and must be updated manually.
                else: 
                    url = pue.PlayerURL(player).findURL()
                    # print(url)
                    print(playerName[0])

                    career = pue.PlayerCareerData(url).careerData()
                    
                    writer.writerow([playerName[0],player,career[0],career[1],career[2],career[3],career[4],career[5],career[6],career[7],career[8],career[9],career[10],career[11],career[12]])

           


            else: 
                url = pue.PlayerURL(player).findURL()
                # print(url)
                print(playerName[0])

                career = pue.PlayerCareerData(url).careerData()
                
                writer.writerow([playerName[0],player,career[0],career[1],career[2],career[3],career[4],career[5],career[6],career[7],career[8],"Null",career[9],career[10],career[11]])
