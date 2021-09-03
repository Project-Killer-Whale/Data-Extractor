class File():

    def __init__(self, parent_path, name, format, data):
        self.parent_path = parent_path
        self.name = name
        self.format = format
        self.data = data

        self.path = parent_path + name + format
