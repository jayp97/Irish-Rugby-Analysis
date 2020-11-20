# This is a script that takes a URL for a specific player and outputs the specific player data relating to the players place of birth. 

import requests
from bs4 import BeautifulSoup
import re 

class RawPlayerData:
    def __init__(self, url):
        self.url = url
    
    def rawPlayerData(self):
        # URL = "http://en.espn.co.uk/ireland/rugby/player/"+str(self.id)+".html"
        URL = self.url 
        print(URL)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id = 'scrumPlayerContent')
        print(results.prettify())

        player_data = results.find_all('b', string='Born')

        print(len(player_data))

        for player in player_data:
            
            raw_born_parent = player.parent
            raw_born = raw_born_parent.text

        return raw_born


        # Does the text contain a county name if yes set county name = to county name
        # if no does text contain an irish/northern Irish city/towm/village name? If yes set city/town/village name property and then search internet/data table for the respective county of that city/town/village.  

# player = RawPlayerData(471)
# print(player.rawPlayerData())
