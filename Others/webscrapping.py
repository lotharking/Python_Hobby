import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Data
players = {'Lionel Messi':'https://www.transfermarkt.com/lionel-messi/profil/spieler/28003'
, 'Cristiano Ronaldo':'https://www.transfermarkt.com/cristiano-ronaldo/profil/spieler/8198'
,'Kylian Mbappe':'https://www.transfermarkt.com/kylian-mbappe/profil/spieler/342229'}

# List
teams = []
estimated_price = []

"""## Test for the code
url = "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.content, 'html.parser')

#WebScraping -- get web and content for price
price = soup.find_all("div", {"class":"tm-player-market-value-development__current-value"})[0].text.strip()

#regular expression
regex_valor = re.compile('\d+\.+\d+')

price = float(regex_valor.search(price)[0])

#WebScraping -- get web and content for team
team = soup.find_all("span", {"class":"data-header__club"})[0].text.strip()

print("precio: "+str(price)+ " y equipo: " + team)
"""
## Test compeleted

regex_valor = re.compile('\d+\.+\d+')

for player in players.keys():
    # Download html
    url = players[player]
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    html = requests.get(url, headers=headers)
    
    # Order the bs
    soup = BeautifulSoup(html.content, 'html.parser')

    # Get team
    team = soup.find_all("span", {"class":"data-header__club"})[0].text.strip()
    teams.append(team)
    
    # Get price
    price = soup.find_all("div", {"class":"tm-player-market-value-development__current-value"})[0].text.strip()
    price = float(regex_valor.search(price)[0])
    estimated_price.append(price)

table = pd.DataFrame({'jugador': list(players.keys())
            , 'equipo' : teams
            , 'valor_mercad_estimado: ': estimated_price})
print(table)