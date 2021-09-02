class FileManager():

    def save_data(file):
        file = open(file.path, "w")
        file.write(file.data)
        file.close()

    def save_file():
        pass

    def read_xlsx_file(file_path, sheet, first_row, columns):
        data = []

        file = openpyxl.load_workbook(PATH)
        sheet = file.active

        for row in range(3, MAX_ROWS + 1):

            cpro = sheet.cell(row=row, column=2).value
            cmun = sheet.cell(row=row, column=3).value
            name = sheet.cell(row=row, column=5).value

            data.append(Town(str(cpro) + str(cmun), unidecode.unidecode(name)))

        return data

    def read_csv_file():
        pass