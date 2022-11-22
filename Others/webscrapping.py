import requests
from bs4 import BeautifulSoup

url = "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
html = requests.get(url, headers=headers)

