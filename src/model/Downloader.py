from src.persistance.JSONFormatter import *
from src.persistance.FileManager import *
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
        beaches =[]

        for id in range(first_beach, last_beach + 1):
            response = requests.get(url + str(id))
            print(response, str(id))

            html = BeautifulSoup(response.text, 'html.parser')
            html_titles = html.find_all('th')
            html_bodies = html.find_all('td')

            data = []

            if html_titles.__len__() != 0:
                for i in range(html_titles.__len__()):
                    data.append(html_bodies[i].text)
            
                beach = BeachInformation()
                beach.assign_object(data, id)
                #beach.__str__()
                beaches.append(beach)
            
            else:
                print("URL no válida: ", url + str(id))
        
        file = File(ou_path, name, format, JSONFormatter.convert_array_object_to_json(beaches)) 
        
        #print(file.path, file.data, file.name)

        FileManager.save_data(file)

        return file