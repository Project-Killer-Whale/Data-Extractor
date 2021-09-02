from src.persistance.JSONFormatter import *  
from src.persistance.FileManager import *
from src.model.Downloader import *
from src.model.Constants import * 
from src.entities.File import *

def main():
    files = download_files()
    read_files(files)
    process_files()
    save_data()

def download_files():

    beach_file = Downloader.download(Constants.URL_BEACHES_FILE, Constants.DATA_PATH, Constants.FILE_NAME_BEACHES, Constants.FILE_TYPE_CSV)
    town_file = Downloader.download(Constants.URL_TOWNS_FILE, Constants.DATA_PATH, Constants.FILE_NAME_TOWNS, Constants.FILE_TYPE_XLSX)

    files = {"Beach": beach_file, "Town": town_file}

    return files

def read_files(files):
    beach_file = files["Beach"]
    town_file = files["Town"]

    beaches_codes = FileManager.read_csv_file(beach_file.path, Constants.CSV_SEPARATOR)
    towns = FileManager.read_xlsx_file(town_file.path, 3, 8133, [2, 3, 5])
    
    return (beaches_codes, towns)

def process_files():
    pass

def save_data():
    pass

main()