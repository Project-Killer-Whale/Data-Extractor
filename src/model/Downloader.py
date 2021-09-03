from src.entities.Beach import *
from src.entities.File import *
from bs4 import BeautifulSoup
from os import path

import requests
import unidecode

class Downloader():

    def download(url, ou_path, name, format):
        path = ou_path + name + format

        request = requests.get(url)
        open(path, 'wb').write(request.content)

        return File(ou_path, name, format, None)

    def download_beach_info(url, ou_path, name, format, first_beach, last_beach):
        path = ou_path + name + format

        beaches =[]

        counter = first_beach
        for beach in range(first_beach, last_beach):

            response = requests.get(url + counter)
            print(response)

            html = BeautifulSoup(response.text, 'html.parser')
            html_titles = html.find_all('th')
            html_bodies = html.find_all('td')

            data = []

            if html_titles.__len__() != 0:
                for i in range(html_titles.__len__()):
                    data.append(html_bodies[i].text)
            
                beach = Beach()
                beach.assign_object(data, counter)
                beaches.append(beach)
            
            else:
                print("URL no válida: ", url)
            
            counter += 1

        return beaches