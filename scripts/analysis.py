import json 

# I want to create a function that takes an input of the county and outputs the total number of players to come from that county

class PlayersPerCounty: 
    def __init__(self, county):
        self.county = county

    
    def ppCounty(self):

        county_count = 0
 
        with open('final-data/irish-player-data.json') as f:
            playerData = json.load(f)

        for i in range(1,len(playerData)):
            
            if playerData[str(i)]["birth place"]['county'] == self.county:
                county_count += 1

        return print(county_count)

PlayersPerCounty("Armagh").ppCounty()

        

        