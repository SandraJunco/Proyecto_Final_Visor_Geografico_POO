from db import db

class institucion(db.Model):
    
    # Nombre de tabla, lo definidos don el atributo __tablename__
    
    __tablename__='instituciones'
    
    # Conjunto de atributos que seran los campos de la tabla 
        # Definir llave primaria: es un campo cuyo valor no se repite en todos los registros de la tabla, sqla.. la define, preferiblemente entero
    id = db.Column(db.Integer, primary_key=True)
    
    # Importante: los campos deben ser objetod de un elemento o una clase columna definida en db 
         #.column() nos permite darle nombre a la columna y el tipo de dato (no den¿finidos en python sino en sqlal...) que va a contener la columna
    
    nombre=db.Column(db.String(80))
    latitud=db.Column(db.Float(20))
    longitud=db.Column(db.Float(20))
    direccion=db.Column(db.String(40))
    horario=db.Column(db.String(20))
    linea_tel=db.Column(db.String(10))
    descripcion=db.Column(db.String(100))
    ruta_imagen=db.Column(db.String(200))
    
    # Método construcctor para mapear datos a los campo definidos
        #Nuestro metodo construcctor va a aceptar varios datos para matearlos a los campos que se realizaron ateriormente
    
    def __init__(self, nombre,latitud, longitud, direccion, horario, linea_tel,descripcion,ruta_imagen):
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud
        self.direccion=direccion
        self.horario=horario
        self.linea_tel=linea_tel
        self.descripcion=descripcion
        self.ruta_imagen=ruta_imagen