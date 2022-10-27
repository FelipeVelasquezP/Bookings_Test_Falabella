from app.modelo.modeloReserva import Reserva
from app.controlador import bp
from flask import Flask,jsonify,request

# app=Flask(__name__)

@bp.route('/',methods=['GET'])
def main():
    return 'Bienvenido a la API REST de Bookings Falabella'


@bp.route('/crearReserva',methods=['POST'])
def crearReserva():
    data = request.get_json()
    return {}


@bp.route('/cancelarReserva',methods=['UPDATE'])
def cancelarReserva():
    return {}


@bp.route('/consultarReservas',methods=['GET'])
def consultarReservas():
    return jsonify(Reserva.conultarReservas(1,2))

def exceptRequest(error):
    return "La petición que intentas realizar es invalida\n"
