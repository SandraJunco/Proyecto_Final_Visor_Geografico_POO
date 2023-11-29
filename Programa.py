from flask import Flask, render_template, request, redirect, url_for
from db import db
from Institucion import institucion

class Programa:
    
    def __init__(self):
        self.app = Flask(__name__)
        
        #craer acceso a una base de datos
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///instituciones.sqlite3'
        
        #Asociamos la base de datos a nuestra aplicacion
        db.init_app(self.app)
                
        # Ruta para mostrar el mapa
        self.app.add_url_rule("/", view_func=self.mostrarMapa, methods=["GET", "POST"])

        # Iniciar el servidor 
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
        
        
    # Renderizado del mapa
    def mostrarMapa(self):
        if request.method == "POST":
            # Aquí puedes agregar el código para manejar los datos del formulario
            # por ejemplo, puedes acceder a los datos como request.form['nombre']
            # y realizar alguna acción con ellos.
            
            #Crear un objeto de la clase institucion con los valores del formulario
            nombre=request.form['nombre']
            latitud=request.form['latitud']
            longitud=request.form['longitud']
            direccion=request.form['direccion']
            horario=request.form['horario']
            linea_tel=request.form['linea_tel']
            descripcion=request.form['descripcion']
            ruta_imagen=request.form['ruta_imagen']
            
            miInstitucion=institucion(nombre, latitud, longitud, direccion, horario, linea_tel,descripcion,ruta_imagen)
            
            #Guardar el objeto en la base de datos
            db.session.add(miInstitucion)
            db.session.commit()
                         
        # Pasar las instituciones a la plantilla    
        return render_template('index.html', instituciones=institucion.query.all())
    
programa = Programa()