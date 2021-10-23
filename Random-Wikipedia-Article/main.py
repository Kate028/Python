import requests
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *

def get_random_article():
    r = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
    content = r.json()
    url = content['content_urls']['desktop']['page']
    title = content['title']
    return title, url

def show_page(url):
    app = QtWidgets.QApplication(sys.argv)
    w = QWebEngineView()
    w.load(QtCore.QUrl(url)) ## load google on startup
    w.showMaximized()
    app.exec_()

while True:
    title, url = get_random_article()
    answer = input('Do you want to read "{}"?(yes/no/quit):'.format(title))
    if answer == 'yes':
        show_page(url)
    elif answer == 'no':
        continue
    break
