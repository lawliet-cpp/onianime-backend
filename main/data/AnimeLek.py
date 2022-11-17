from bs4 import BeautifulSoup
import requests

class Animelek(object):
    def __init__(self,anime_name):
        self.anime_name = anime_name
        

    def get_download_link(self,episode):
        response = requests.get(f'https://animelek.me/episode/{self.anime_name}-{episode}-الحلقة')
    
        soup = BeautifulSoup(response.content,'html5lib')
        soup.prettify()
        downloads = soup.find('div',attrs={'id':'downloads'})

        links = downloads.find_all('li',attrs={'class':'watch'})
        download_links = []
        for link in links:
            anime = {
                'link':link.a["href"],
                'name':link.a.text
            }
            download_links.append(anime)

        return download_links



