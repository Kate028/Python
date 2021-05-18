import requests
import bs4
from bs4 import BeautifulSoup

page = requests.get('https://www.amazon.in/Raspberry-Pi-Model-RASP-PI-3-Motherboard/dp/B01CD5VC92')
soup = BeautifulSoup(page.content, 'html.parser')

rasp = soup.find(id = 'featurebullets_feature_div')

items = rasp.find_all(class_ = 'a-list-item')

print(items[0])
# print(rasp)
# print(items[0].find(class_= 'class="a-list-item"').get_text())