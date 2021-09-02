from src.entities.Town import *

import openpyxl
import unidecode

class FileManager():

    def save_data(file):
        file = open(file.path, "w")
        file.write(file.data)
        file.close()

    def save_file():
        pass

    def read_xlsx_file(file_path, first_row, last_row, columns):
        data = []

        file = openpyxl.load_workbook(file_path)
        sheet = file.active

        for row in range(first_row, last_row + 1):

            cpro = sheet.cell(row=row, column=columns[0]).value
            cmun = sheet.cell(row=row, column=columns[1]).value
            name = sheet.cell(row=row, column=columns[2]).value

            data.append(Town(str(cpro) + str(cmun), unidecode.unidecode(name)))

        return data

    def read_csv_file(file_path, separator):
        file = open(file_path, 'r')
        content = file.read()
        print(content)
        file.close()