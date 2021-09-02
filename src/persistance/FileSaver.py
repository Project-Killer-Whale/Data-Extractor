class FileSaver():

    def __init__(self):
        pass

    def save_data(self, file):
        file = open(file.path, "w")
        file.write(file.data)
        file.close()