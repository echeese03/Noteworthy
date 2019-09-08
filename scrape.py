from bs4 import BeautifulSoup
import requests
import urllib.request
import random

url = "https://www.usnews.com/topics/subjects/students"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

def random_news_article():
    soup = BeautifulSoup(response.text, "html.parser")

    x = soup.findAll("a", {"class": "Anchor-u1fur6-0 chvEFD"})

    x = x[9:len(x) - 16]

    links = [l['href'] for l in x]

    return random.choice(links)

