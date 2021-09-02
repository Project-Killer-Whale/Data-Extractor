from os import path
import requests

class Downloader():

    def download(url, ou_path, name, format):
        path = ou_path + name + format

        request = requests.get(url)
        open(path, 'wb').write(request.content)

        return True