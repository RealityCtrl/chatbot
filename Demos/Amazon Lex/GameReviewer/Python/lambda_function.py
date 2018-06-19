from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    # TODO implement
    baseUrl = 'http://www.metacritic.com/game/pc/'
    game = event['currentIntent']['slots']['Game'].title()
    url = baseUrl+game

    #make request to metacritic
    request = Request(url,headers={'User-Agent': 'Mozilla/5.0'}) #this user agent is to stop our scrape from being blocked by metacritic
    htmlData = urlopen(request).read()

    #bring me some soup
    #stick the html into BeautifulSoup4
    soup = BeautifulSoup(htmlData, 'html.parser')
    #find the rating from the metacritic page and return it
    return soup.findAll("span", {"itemprop": "ratingValue"})[0].string
