from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import random
import lxml
# list of Episodes and Teasers
episodes = []

teasers = []

# List of URLs

urls = [f"https://binnenstebuiten.kro-ncrv.nl/terugkijken?show=1&jaar=all&page={i}" for i in range(0,92)]

# List of Randomizing our request rate

rate = [i/10 for i in range(10)]

# Iterating through the URLs

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    episodes.extend([i.text for i in soup.find_all(class_="teaser__title")])
    teasers.extend([i.text for i in soup.find_all(class_="teaser__summary")])
    if len(teasers) >= 3000:
        break
    time.sleep(random.choice(rate))

df = pd.DataFrame()
df['Episodes'] = episodes
df['Teasers'] = teasers
df.to_csv(r'bb_teasers.csv')