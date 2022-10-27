from flask import Flask
from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from app.controlador import bp as controlador_bp
  app.register_blueprint(controlador_bp)
  return app


from app.modelo.modeloReserva import Reserva
from app.modelo.modeloHotel import Hotel
from app.modelo.modeloUsuario import Usuario
