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
        print(
            "ID:\t", self.id,
            "NOMBRE:\t", self.nombre,
            "ID MUNICIPIO:\t", self.id_municipio,
            "MUNICIPIO:\t", self.municipio,
            "ID PROVINCIA:\t", self.id_provincia,
            "PROVINCIA:\t", self.provincia,
            "LATITUD:\t", self.latitud,
            "LONGITUD:\t", self.longitud,
            )