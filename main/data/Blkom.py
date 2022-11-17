from urllib import response
import requests
from bs4 import BeautifulSoup
class Blkom(object):

    def __init__(self,anime_name,episode) -> None:
        self.anime_name = anime_name
        self.episode = episode
        self.base_link = "https://animeblkom.net"




    def get_anime_watch_link(self,query,episode):

        response = requests.get(self.base_link + '/search?query='+query)

        soup = BeautifulSoup(response.content,'html5lib')

        soup.prettify()


        anime_div = soup.find('div',attrs={'class':'name'})
        link = anime_div.a['href']
        response2 = requests.get(f'{self.base_link}{link}/{str(episode)}')
        print(response2.content)
        soup2 = BeautifulSoup(response2.content,'html5lib')
        iframe = soup2.find('iframe')

        return iframe['src']

        


    

