class Constants():
    
    PATH = "./"
    OU_PATH = PATH + "output/"
    DATA_PATH = PATH + "data/"

    FILE_TYPE_JSON = ".json"
    FILE_TYPE_TXT = ".txt"
    FILE_TYPE_CSV = ".csv"
    FILE_TYPE_XLSX = ".xlsx"

    URL_BEACHES_FILE = "http://www.aemet.es/documentos/es/eltiempo/prediccion/playas/Playas_codigos.csv"
    URL_TOWNS_FILE = "https://www.ine.es/daco/daco42/codmun/codmun20/20codmun.xlsx"
    URL_BEACHES_INFORMATION = "https://sig.mapama.gob.es/WebServices/clientews/Guia-Playas/default.aspx?origen=1010&nombre=PLAYAS&claves=DGC.PLAYAS.PLY_CO_PLAYA&valores="

    FILE_NAME_BEACHES = "Beach_codes" 
    FILE_NAME_TOWNS = "Town_codes"
    FILE_NAME_BEACH_INFO = "Beach_info"

    CSV_SEPARATOR = ";"
    
    FIRST_BEACH_INFO = 1
    LAST_BEACH_INFO = 3112