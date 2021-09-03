import unidecode

class BeachInformation():
    
    def __init__(self):
        self.id = ""
        self.nombre = ""
        self.municipio = ""
        self.provincia = ""
        self.comunidad_autonoma = ""
        self.longitud = ""
        self.anchura = ""
        self.grado_ocupacion = ""
        self.grado_urbanizacion = ""
        self.paseo_maritimo = ""
        self.fachada_litoral = ""
        self.descripcion = ""
        self.composicion = ""
        self.tipo_arena = ""
        self.condiciones = ""
        self.zona_fondeo = ""
        self.nudismo = ""
        self.vegetacion = ""
        self.espacio_protegido = ""
        self.actuaciones = ""
        self.bandera_azul = ""
        self.nombre_hospital = ""
        self.direccion = ""
        self.telefono_hospital = ""
        self.distancia_aproximada_a_playa = ""
        self.forma_de_acceso = ""
        self.senalizacion_de_los_accesos = ""
        self.acceso_discapacitados = ""
        self.coordenadas  = ""
        self.coordenadas_utm = ""
        self.senalizacion_de_peligro = ""
        self.auxilio_y_salvamento = ""
        self.carretera_mas_proxima = ""
        self.autobus = ""
        self.aparcamiento = ""
        self.nombre_puerto = ""
        self.distancia_aproximada_a_puerto = ""
        self.aseos = ""
        self.lavapies = ""
        self.duchas = ""
        self.papeleras = ""
        self.servicio_limpieza = ""
        self.oficina_turismo = ""
        self.telefono = ""
        self.establecimiento_comida = ""
        self.establecimiento_bebida = ""
        self.alquiler_hamacas = ""
        self.alquiler_sombrillas = ""
        self.alquiler_nauticos = ""
        self.club_nautico = ""
        self.zona_submarinismo = ""
        self.zona_practica_de_surf = ""
        self.zona_infantil = ""
        self.zona_deportiva = ""
    
    def assign_object(self, data, counter):
            self.id = counter
            self.nombre = unidecode.unidecode(data[0])
            self.municipio = unidecode.unidecode(data[1])
            self.provincia = unidecode.unidecode(data[2])
            self.comunidad_autonoma = unidecode.unidecode(data[3])
            self.longitud = unidecode.unidecode(data[4])
            self.anchura = unidecode.unidecode(data[5])
            self.grado_ocupacion = unidecode.unidecode(data[6])
            self.grado_urbanizacion = unidecode.unidecode(data[7])
            self.paseo_maritimo = unidecode.unidecode(data[8])
            self.fachada_litoral = unidecode.unidecode(data[9])
            self.descripcion = unidecode.unidecode(data[10])
            self.composicion = unidecode.unidecode(data[11])
            self.tipo_arena = unidecode.unidecode(data[12])
            self.condiciones = unidecode.unidecode(data[13])
            self.zona_fondeo = unidecode.unidecode(data[14])
            self.nudismo = unidecode.unidecode(data[15])
            self.vegetacion = unidecode.unidecode(data[16])
            self.espacio_protegido = unidecode.unidecode(data[17])
            self.actuaciones = unidecode.unidecode(data[18])
            self.bandera_azul = unidecode.unidecode(data[19])
            self.nombre_hospital = unidecode.unidecode(data[20])
            self.direccion = unidecode.unidecode(data[21])
            self.telefono_hospital = unidecode.unidecode(data[22])
            self.distancia_aproximada_a_playa = unidecode.unidecode(data[23])
            self.forma_de_acceso = unidecode.unidecode(data[24])
            self.senalizacion_de_los_accesos = unidecode.unidecode(data[25])
            self.acceso_discapacitados = unidecode.unidecode(data[26])
            self.coordenadas  = unidecode.unidecode(data[27])
            self.coordenadas_utm = unidecode.unidecode(data[28])
            self.senalizacion_de_peligro = unidecode.unidecode(data[29])
            self.auxilio_y_salvamento = unidecode.unidecode(data[30])
            self.carretera_mas_proxima = unidecode.unidecode(data[31])
            self.autobus = unidecode.unidecode(data[32])
            self.aparcamiento = unidecode.unidecode(data[33])
            self.nombre_puerto = unidecode.unidecode(data[34])
            self.distancia_aproximada_a_puerto = unidecode.unidecode(data[35])
            self.aseos = unidecode.unidecode(data[36])
            self.lavapies = unidecode.unidecode(data[37])
            self.duchas = unidecode.unidecode(data[38])
            self.papeleras = unidecode.unidecode(data[39])
            self.servicio_limpieza = unidecode.unidecode(data[40])
            self.oficina_turismo = unidecode.unidecode(data[41])
            self.telefono = unidecode.unidecode(data[42])
            self.establecimiento_comida = unidecode.unidecode(data[43])
            self.establecimiento_bebida = unidecode.unidecode(data[44])
            self.alquiler_hamacas = unidecode.unidecode(data[45])
            self.alquiler_sombrillas = unidecode.unidecode(data[46])
            self.alquiler_nauticos = unidecode.unidecode(data[47])
            self.club_nautico = unidecode.unidecode(data[48])
            self.zona_submarinismo = unidecode.unidecode(data[49])
            self.zona_practica_de_surf = unidecode.unidecode(data[50])
            self.zona_infantil = unidecode.unidecode(data[51])
            self.zona_deportiva = unidecode.unidecode(data[52])
    def __str__(self):
        print(
        self.id,
        self.nombre,
        self.municipio,
        self.provincia,
        self.comunidad_autonoma,
        self.longitud,
        self.anchura,
        self.grado_ocupacion,
        self.grado_urbanizacion,
        self.paseo_maritimo,
        self.fachada_litoral,
        self.descripcion,
        self.composicion,
        self.tipo_arena,
        self.condiciones,
        self.zona_fondeo,
        self.nudismo,
        self.vegetacion,
        self.espacio_protegido,
        self.actuaciones,
        self.bandera_azul,
        self.nombre_hospital,
        self.direccion,
        self.telefono_hospital,
        self.distancia_aproximada_a_playa,
        self.forma_de_acceso,
        self.senalizacion_de_los_accesos,
        self.acceso_discapacitados,
        self.coordenadas ,
        self.coordenadas_utm,
        self.senalizacion_de_peligro,
        self.auxilio_y_salvamento,
        self.carretera_mas_proxima,
        self.autobus,
        self.aparcamiento,
        self.nombre_puerto,
        self.distancia_aproximada_a_puerto,
        self.aseos,
        self.lavapies,
        self.duchas,
        self.papeleras,
        self.servicio_limpieza,
        self.oficina_turismo,
        self.telefono,
        self.establecimiento_comida,
        self.establecimiento_bebida,
        self.alquiler_hamacas,
        self.alquiler_sombrillas,
        self.alquiler_nauticos,
        self.club_nautico,
        self.zona_submarinismo,
        self.zona_practica_de_surf,
        self.zona_infantil,
        self.zona_deportiva
        )