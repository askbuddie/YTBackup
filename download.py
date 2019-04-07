import urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube

import os
import json


# get the title of the videos
def getVideo(title):
    query = urllib.parse.quote(title)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href']


with open("./tree.json") as f:
    data = json.load(f)
    for i in data:
        title = os.path.basename(i)
        dirname = os.path.dirname(i)
        print(dirname)
        os.makedirs(dirname)
        YouTube(getVideo(title)).streams.first().download(dirname)
