import requests
from bs4 import BeautifulSoup
import re 
import csv

# I need to make a function now that loops through the csv containing raw player data and adds in the player name to this function. This function outputs the URL which is then fed into the player-data-scraper which outputs the raw players birth place data. 

# ---------------------------------------------------------------------------------------------------------

# I need a function that takes an input of Player name. The function looks for id=scrumPlayer content. it then looks for a <b> that contains the Player name. It then returns the string/text of the href of the parent <a>. 
# This string is then fed into the current function above. (I basically just change the input from id to URL, otherwise its just the same class, only a different input)

class PlayerURL: 
    def __init__(self, player):
        self.player = player

    
    def findURL(self):
        URL = "http://en.espn.co.uk/ireland/rugby/player/caps.html?team=3"
        # print(URL)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id = 'scrumPlayerContent')
        # print(results.prettify())

        player_data = results.find_all('b', string=self.player)

        # print(len(player_data))

        for player in player_data:
            
            
            player_parent = player.parent

        # print(player_parent)
        # print(player_parent.get("href"))
        hrefPlayer = player_parent.get("href")
        urlOfPlayer = "http://en.espn.co.uk"+hrefPlayer+"" 
        return urlOfPlayer


# ---------------------------------------------------------------------------------------------------------

class RawPlayerData:
    def __init__(self, url):
        self.url = url
    
    def rawPlayerData(self):
        # URL = "http://en.espn.co.uk/ireland/rugby/player/"+str(self.id)+".html"
        URL = self.url 
        # print(URL)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id = 'scrumPlayerContent')
        # print(results.prettify())

        player_data = results.find_all('b', string='Born')

        # print(len(player_data))

        for player in player_data:
            
            raw_born_parent = player.parent
            raw_born = raw_born_parent.text

        return raw_born


# ---------------------------------------------------------------------------------------------------------

class PlayerCareerData:
    def __init__(self, url):
        self.url = url
    
    def careerData(self):

        URL = self.url 
        print(URL)
        page = requests.get(URL)
        careerList = []

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find("tr", class_ = 'data1')
        print(results.prettify())

        career_data = results.find_all('td')

        print(len(career_data))

        for career in career_data:
            
            # raw_born_parent = player.parent
            # raw_born = raw_born_parent.text
            
            careerList.append(career.text)

        careerList = careerList[1:-1]
        print(careerList)
        
        return careerList







# ---------------------------------------------------------------------------------------------------------

        # Does the text contain a county name if yes set county name = to county name
        # if no does text contain an irish/northern Irish city/towm/village name? If yes set city/town/village name property and then search internet/data table for the respective county of that city/town/village.  

# ---------------------------------------------------------------------------------------------------------


# with open('raw/raw-player-data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["No.", "Player", "Position", "Debut", "Raw-Birth-Data"])

#     rawName = csv.reader(open('raw/raw-player-data-espn.csv','r'))

#     for row in rawName:
#         # if row[1] == "Henry Walsh":
#         #     exit()

#         if row[1] == "Player":
#             pass 

#         else:
#             playerName = row[1].strip()
#             print(playerName)

#             urlPlayer = PlayerURL(playerName).findURL()
#             # print(urlPlayer)

#             rawData = RawPlayerData(urlPlayer).rawPlayerData()
#             print(rawData)

#             writer.writerow([row[0], playerName, row[2].strip(), row[3].strip(), rawData])



