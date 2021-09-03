from src.persistance.JSONFormatter import *  
from src.persistance.FileManager import *
from src.model.Downloader import *
from src.model.Constants import * 
from src.entities.File import *

def main():
    files = download_files()
    files = read_files(files)
    data = process_files(files)
    save_data(data)

def download_files():

    beach_info_file_path = Constants.DATA_PATH + Constants.FILE_NAME_BEACH_INFO + Constants.FILE_TYPE_JSON

    beach_file = Downloader.download(Constants.URL_BEACHES_FILE, Constants.DATA_PATH, Constants.FILE_NAME_BEACHES, Constants.FILE_TYPE_CSV)
    town_file = Downloader.download(Constants.URL_TOWNS_FILE, Constants.DATA_PATH, Constants.FILE_NAME_TOWNS, Constants.FILE_TYPE_XLSX)
    
    if FileManager.check_if_exists(beach_info_file_path):
        print("Beach info file already downloaded")
        beach_info_file = File(Constants.DATA_PATH, Constants.FILE_NAME_BEACH_INFO, Constants.FILE_TYPE_JSON, FileManager.read_txt_file(beach_info_file_path))
    else: 
        beach_info_file = Downloader.download_beach_info(Constants.URL_BEACHES_INFORMATION, Constants.DATA_PATH, Constants.FILE_NAME_BEACH_INFO, Constants.FILE_TYPE_JSON, Constants.FIRST_BEACH_INFO, Constants.LAST_BEACH_INFO)
    
    files = {"Beach": beach_file, "Town": town_file, "Beach_info": beach_info_file}

    return files

def read_files(files):
    beach_file = files["Beach"]
    town_file = files["Town"]
    beach_info_file = files["Beach_info"]

    beaches_codes = FileManager.read_csv_file(beach_file.path, Constants.CSV_SEPARATOR)
    towns = FileManager.read_xlsx_file(town_file.path, 3, 8133, [2, 3, 5])
    beaches_info = FileManager.read_json_file(beach_info_file.path)

    return (beaches_codes, towns, beaches_info)

def process_files(files):
    data = []

    beaches_codes = files[0]
    towns_codes = files[1]
    beaches_info = files[2]

    for beach_info in beaches_info:
        
        for town in towns_codes:
            if beach_info.municipio == town.name:
                beach_info.town_code = town.cod
        
        beach = Beach(beach_info.id, beach_info, None)
        
        for beach_cod in beaches_codes:
            if beach_info.nombre == beach_cod.nombre and beach_info.municipio == beach_cod.municipio and beach_info.provincia == beach_cod.provincia:
                beach.beach_code = beach_cod.id
        
        data.append(beach)
    
    return data

def save_data(data):
    print(data[0])
    FileManager.save_data(File(Constants.OU_PATH, Constants.FILE_NAME_OUTPUT, Constants.FILE_TYPE_JSON, JSONFormatter.convert_array_object_to_json(data)))

main()