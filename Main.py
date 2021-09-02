from typing import Container
from src.persistance.JSONFormatter import *  
from src.persistance.FileManager import *
from src.model.Downloader import *
from src.model.Constants import * 

def main():
    download_files()
    read_files()
    process_files()
    save_data()

def download_files():
    Downloader.download(Constants.URL_BEACHES_FILE, Constants.DATA_PATH, "Beach_codes", Constants.FILE_TYPE_CSV)
    Downloader.download(Constants.URL_TOWNS_FILE, Constants.DATA_PATH, "Town_codes", Constants.FILE_TYPE_XLSX)

def read_files():
    pass

def process_files():
    pass

def save_data():
    pass

main()