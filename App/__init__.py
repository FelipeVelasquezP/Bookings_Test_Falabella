"""
Archivo: __init__.py
Descripción: Este es el lugar donde Flask Arranca la aplicacioón empaquetando todos los datos nesesarios para acción
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""

#Se importan las bibliotecas nesesarias
from flask import Flask
from config import Config

""" Función que inicia a aplicacion de flask:
    @ config_class: Archivo de configuracion inicial
    Retorna : la appp inicializada
"""
def create_app(config_class=Config):
  app = Flask(__name__) # crea la app
  app.config.from_object(config_class) #inicializa con los datos de configuración
  from app.controlador import bp as controlador_bp #Se importa el modulo de direccionamiento
  app.register_blueprint(controlador_bp)# Se crea el empaquetamiento para los controladores
  return app # retorna la app

#Se importan todos los modelos ue se utilizan en l aplicaión
from app.modelo.modeloReserva import Reserva
from app.modelo.modeloHotel import Hotel
from app.modelo.modeloUsuario import Usuario
from app.modelo.modeloHabitacion import Habitacion
