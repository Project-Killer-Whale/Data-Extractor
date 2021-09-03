from src.entities.BeachInformation import *

class Beach():

    def __init__(self):
        pass

    def __init__(self, id):
        self.id = id
    
    def __init__(self, id, beach_information, beach_code):
        self.id = id
        self.beach_information = beach_information
        self.beach_code = beach_code