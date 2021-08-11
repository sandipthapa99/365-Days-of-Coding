import requests
from bs4 import BeautifulSoup

# website to fetch links from
url = 'https://www.sandipthapa.com.np/'

# get contents from the website
fetcher = requests.get(url).content
soupObj = BeautifulSoup(fetcher, 'html.parser')
links = soupObj.find_all('a')

for link in links:
    # if link present in <a> tag print it
    try:
        print(link['href'])
    # if link not present in <a> tag go to next tag
    except:
        continue

# --------
# Result:
# --------------------------------------------------------
# https://www.linkedin.com/in/sandipthapa99/
# https://www.facebook.com/sandipthapa99
# https://twitter.com/sandipthapa99
# https://github.com/sandipthapa99
# https://heraldcollege.edu.np/
# https://www.bernhardt.edu.np/
# https://www.facebook.com/skylordnepal/
# https://github.com/sandipthapa99/portfolio
# https://github.com/sandipthapa99/Tic-Tac-Toe-Python-GUI
# https://github.com/sandipthapa99/Smart_Calculator
# https://github.com/sandipthapa99/Quiz-Web-App
# https://github.com/sandipthapa99/audioroot
# https://github.com/sandipthapa99/Regression
# --------------------------------------------------------