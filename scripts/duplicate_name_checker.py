import csv

playerList = csv.reader(open('data/player-data-country.csv','r')) 


# name = "Bill"
duplicates = []

for player in playerList: 
    playerNames = csv.reader(open('data/player-data-country.csv','r')) 
    for playerName in playerNames:
        if playerName[1] == player[1] and playerName[0] != player[0]: 
            duplicates.append(playerName[1])
            
print(duplicates)

names = ['Edward MacIlwaine', 'Robert Morrow', 'William Collis', 'John Fitzgerald', 'James Stevenson', 'Edward MacIlwaine', "Jack O'Connor", 'John Ryan', 'William Brown', "Jack O'Connor", 'Michael Bradley', 'William Collis', 'Noel Murphy', 'Patrick Lawlor', 'James Ryan', 'Patrick Lawlor', 'John Hewitt', 'Noel Murphy', 'James Stevenson', 'William Brown', 'Denis Hickie', 'John Murphy', 'John Hewitt', 'Michael Bradley', 'Robert Morrow', 'John Fitzgerald', 'John Murphy', 'Denis Hickie', 'John Ryan', 'James Ryan']

numbers = ['229', '832', '440', '841', '657', '15', '331', '1088', '731', '231', '825', '114', '656', '597', '1095', '517', '810', '481', '171', '253', '924', '883', '620', '402', '93', '116', '809', '735', '241', '542']








