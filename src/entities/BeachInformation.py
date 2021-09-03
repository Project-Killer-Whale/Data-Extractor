import unidecode

class BeachInformation():
    
    def __init__(self):
        self.id = ""
        self.beach_id = ""
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
        self.town_code = ""
    
    def assign_object_dict(self, data):
            self.id = data.id
            self.nombre = unidecode.unidecode(data.nombre)
            self.municipio = unidecode.unidecode(data.municipio)
            self.provincia = unidecode.unidecode(data.provincia)
            self.comunidad_autonoma = unidecode.unidecode(data.comunidad_autonoma)
            self.longitud = unidecode.unidecode(data.longitud)
            self.anchura = unidecode.unidecode(data.anchura)
            self.grado_ocupacion = unidecode.unidecode(data.grado_ocupacion)
            self.grado_urbanizacion = unidecode.unidecode(data.grado_urbanizacion)
            self.paseo_maritimo = unidecode.unidecode(data.paseo_maritimo)
            self.fachada_litoral = unidecode.unidecode(data.fachada_litoral)
            self.descripcion = unidecode.unidecode(data.descripcion)
            self.composicion = unidecode.unidecode(data.composicion)
            self.tipo_arena = unidecode.unidecode(data.tipo_arena)
            self.condiciones = unidecode.unidecode(data.condiciones)
            self.zona_fondeo = unidecode.unidecode(data.zona_fondeo)
            self.nudismo = unidecode.unidecode(data.nudismo)
            self.vegetacion = unidecode.unidecode(data.vegetacion)
            self.espacio_protegido = unidecode.unidecode(data.espacio_protegido)
            self.actuaciones = unidecode.unidecode(data.actuaciones)
            self.bandera_azul = unidecode.unidecode(data.bandera_azul)
            self.nombre_hospital = unidecode.unidecode(data.nombre_hospital)
            self.direccion = unidecode.unidecode(data.direccion)
            self.telefono_hospital = unidecode.unidecode(data.telefono_hospital)
            self.distancia_aproximada_a_playa = unidecode.unidecode(data.distancia_aproximada_a_playa)
            self.forma_de_acceso = unidecode.unidecode(data.forma_de_acceso)
            self.senalizacion_de_los_accesos = unidecode.unidecode(data.senalizacion_de_los_accesos)
            self.acceso_discapacitados = unidecode.unidecode(data.acceso_discapacitados)
            self.coordenadas  = unidecode.unidecode(data.coordenadas)
            self.coordenadas_utm = unidecode.unidecode(data.coordenadas_utm)
            self.senalizacion_de_peligro = unidecode.unidecode(data.senalizacion_de_peligro)
            self.auxilio_y_salvamento = unidecode.unidecode(data.auxilio_y_salvamento)
            self.carretera_mas_proxima = unidecode.unidecode(data.carretera_mas_proxima)
            self.autobus = unidecode.unidecode(data.autobus)
            self.aparcamiento = unidecode.unidecode(data.aparcamiento)
            self.nombre_puerto = unidecode.unidecode(data.nombre_puerto)
            self.distancia_aproximada_a_puerto = unidecode.unidecode(data.distancia_aproximada_a_puerto)
            self.aseos = unidecode.unidecode(data.aseos)
            self.lavapies = unidecode.unidecode(data.lavapies)
            self.duchas = unidecode.unidecode(data.duchas)
            self.papeleras = unidecode.unidecode(data.papeleras)
            self.servicio_limpieza = unidecode.unidecode(data.servicio_limpieza)
            self.oficina_turismo = unidecode.unidecode(data.oficina_turismo)
            self.telefono = unidecode.unidecode(data.telefono)
            self.establecimiento_comida = unidecode.unidecode(data.establecimiento_comida)
            self.establecimiento_bebida = unidecode.unidecode(data.establecimiento_bebida)
            self.alquiler_hamacas = unidecode.unidecode(data.alquiler_hamacas)
            self.alquiler_sombrillas = unidecode.unidecode(data.alquiler_sombrillas)
            self.alquiler_nauticos = unidecode.unidecode(data.alquiler_nauticos)
            self.club_nautico = unidecode.unidecode(data.club_nautico)
            self.zona_submarinismo = unidecode.unidecode(data.zona_submarinismo)
            self.zona_practica_de_surf = unidecode.unidecode(data.zona_practica_de_surf)
            self.zona_infantil = unidecode.unidecode(data.zona_infantil)
            self.zona_deportiva = unidecode.unidecode(data.zona_deportiva)
            
    
    def assign_object(self, data):
            self.id = unidecode.unidecode(data[0])
            self.nombre = unidecode.unidecode(data[1])
            self.municipio = unidecode.unidecode(data[2])
            self.provincia = unidecode.unidecode(data[3])
            self.comunidad_autonoma = unidecode.unidecode(data[4])
            self.longitud = unidecode.unidecode(data[5])
            self.anchura = unidecode.unidecode(data[6])
            self.grado_ocupacion = unidecode.unidecode(data[7])
            self.grado_urbanizacion = unidecode.unidecode(data[8])
            self.paseo_maritimo = unidecode.unidecode(data[9])
            self.fachada_litoral = unidecode.unidecode(data[10])
            self.descripcion = unidecode.unidecode(data[11])
            self.composicion = unidecode.unidecode(data[12])
            self.tipo_arena = unidecode.unidecode(data[13])
            self.condiciones = unidecode.unidecode(data[14])
            self.zona_fondeo = unidecode.unidecode(data[15])
            self.nudismo = unidecode.unidecode(data[16])
            self.vegetacion = unidecode.unidecode(data[17])
            self.espacio_protegido = unidecode.unidecode(data[18])
            self.actuaciones = unidecode.unidecode(data[19])
            self.bandera_azul = unidecode.unidecode(data[20])
            self.nombre_hospital = unidecode.unidecode(data[21])
            self.direccion = unidecode.unidecode(data[22])
            self.telefono_hospital = unidecode.unidecode(data[23])
            self.distancia_aproximada_a_playa = unidecode.unidecode(data[24])
            self.forma_de_acceso = unidecode.unidecode(data[25])
            self.senalizacion_de_los_accesos = unidecode.unidecode(data[26])
            self.acceso_discapacitados = unidecode.unidecode(data[27])
            self.coordenadas  = unidecode.unidecode(data[28])
            self.coordenadas_utm = unidecode.unidecode(data[29])
            self.senalizacion_de_peligro = unidecode.unidecode(data[30])
            self.auxilio_y_salvamento = unidecode.unidecode(data[31])
            self.carretera_mas_proxima = unidecode.unidecode(data[32])
            self.autobus = unidecode.unidecode(data[33])
            self.aparcamiento = unidecode.unidecode(data[34])
            self.nombre_puerto = unidecode.unidecode(data[35])
            self.distancia_aproximada_a_puerto = unidecode.unidecode(data[36])
            self.aseos = unidecode.unidecode(data[37])
            self.lavapies = unidecode.unidecode(data[38])
            self.duchas = unidecode.unidecode(data[39])
            self.papeleras = unidecode.unidecode(data[40])
            self.servicio_limpieza = unidecode.unidecode(data[41])
            self.oficina_turismo = unidecode.unidecode(data[42])
            self.telefono = unidecode.unidecode(data[43])
            self.establecimiento_comida = unidecode.unidecode(data[44])
            self.establecimiento_bebida = unidecode.unidecode(data[45])
            self.alquiler_hamacas = unidecode.unidecode(data[46])
            self.alquiler_sombrillas = unidecode.unidecode(data[47])
            self.alquiler_nauticos = unidecode.unidecode(data[48])
            self.club_nautico = unidecode.unidecode(data[49])
            self.zona_submarinismo = unidecode.unidecode(data[50])
            self.zona_practica_de_surf = unidecode.unidecode(data[51])
            self.zona_infantil = unidecode.unidecode(data[52])
            self.zona_deportiva = unidecode.unidecode(data[53])
        
    def __str__(self):
        print(
        self.id,
        self.beach_id,
        self.nombre,
        self.town_code,
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