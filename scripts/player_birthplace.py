from .player_data_scraper import RawPlayerData
from .player_url_extractor import PlayerURL

# I need to make a function now that loops through the csv containing raw player data and adds in the player name to this function. This function outputs the URL which is then fed into the player-data-scraper which outputs the raw players birth place data. 


url = PlayerURL("William Allen")
print(url)

rawData = RawPlayerData(url)

print(rawData)