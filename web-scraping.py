import requests
import bs4
from bs4 import BeautifulSoup
page = requests.get('https://www.amazon.in/Raspberry-Pi-Model-RASP-PI-3-Motherboard/dp/B01CD5VC92')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
