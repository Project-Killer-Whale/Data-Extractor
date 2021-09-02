class FileSaver():

    def __init__(self):
        pass

    def save_data(self, path, data, format):
        file = open(path + "." + , "w")
        file.write(data)
        file.close()