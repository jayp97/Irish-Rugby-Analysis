import requests
from bs4 import BeautifulSoup
import re 

URL = 'http://en.espn.co.uk/ireland/rugby/player/471.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id = 'scrumPlayerContent')
print(results.prettify())

# player_data = results.find_all('div', class_='scrumPlayerDesc')
# player_data = results.find_all('div', string=lambda text: 'born' in text.lower())
# player_data = results.find_all(string=re.compile("Born"))
player_data = results.find_all('b', string='Born')


print(len(player_data))

for player in player_data:
    
    # print(player.parent, end='\n'*2)
    raw_born_parent = player.parent
    raw_born = raw_born_parent.text
    # place_of_birth = player.find('div', string=lambda text: 'born' in text.lower())

print(raw_born, end='\n'*2)
print(type(raw_born))
print("galway" in raw_born.lower())

# Does the text contain a county name if yes set county name = to county name
# if no does text contain an irish/northern Irish city/towm/village name? If yes set city/town/village name property and then search internet/data table for the respective county of that city/town/village.  
