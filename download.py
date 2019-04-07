# import urllib.request
# from bs4 import BeautifulSoup
# from pytube import YouTube

import os
import json

with open("./testfolder.json") as f:
    data = json.load(f)
    for x in data:
        for xx in data[x]:
            print(xx)


def safe_make_folder(i):
    """Makes a folder (and its parents) if not present"""
    try:
        os.makedirs(i)
    except:
        pass


# safe_make_folder("red")

# def getVideo(title):
#   query = urllib.parse.quote(title)
#   url = "https://www.youtube.com/results?search_query=" + query
#   response = urllib.request.urlopen(url)
#   html = response.read()
#   soup = BeautifulSoup(html, 'html.parser')
#   return soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

# YouTube(getVideo('5 ways to vertically center with CSS.mp4')).streams.first().download('./tuts/')
