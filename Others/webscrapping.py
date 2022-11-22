import requests
from bs4 import BeautifulSoup
import re

url = "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.content, 'html.parser')

#WebScraping -- get web and content for price
price = soup.find_all("div", {"class":"tm-player-market-value-development__current-value"})[0].text.strip()

#regular expression
regex_valor = re.compile('\d+\.+\d+')

price = float(regex_valor.search(price)[0]) #price

#WebScraping -- get web and content for team
team = soup.find_all("span", {"class":"data-header__club"})[0].text.strip()

print("precio: "+str(price)+ " y equipo: " + team)