class BeachCode():

    def __init__(self, id, nombre, id_municipio, municipio, id_provincia, provincia, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.id_municipio = id_municipio
        self.municipio = municipio
        self.id_provincia = id_provincia
        self.provincia = provincia
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return "ID:", self.id + " " + "NOMBRE:" + " " + self.nombre + " " + "ID MUNICIPIO:" + " " + self.id_municipio + " " + "MUNICIPIO:" + " " + self.municipio + " " + "ID PROVINCIA:" + " " + self.id_provincia + " " + "PROVINCIA:" + " " + self.provincia + " " + "LATITUD:" + " " + self.latitud + " " + "LONGITUD:" + " " + self.longitud
        