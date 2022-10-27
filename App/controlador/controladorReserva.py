from ast import Return
from app.modelo.modeloReserva import Reserva
from app.controlador import bp
from flask import Flask,jsonify,request
import datetime

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
    data = request.get_json()
    checkin=data.get('checkin')
    checkout=data.get('checkout')
    if validarFechas(checkin,checkout):
        reservas=Reserva.conultarReservas(checkin,checkout,data.get('idHotel'))
        return jsonify({'reservas':reservas,'DataProperties':"Success"})
    else:
        return jsonify({'reservas':[],'DataProperties':"Error","descripcion":"checkout debe ser mayor a checkin"})
        

def formatearFecha(fecha):
    indices=fecha.split('-')
    return datetime.datetime(int(indices[0]),int(indices[1]), int(indices[2])) 

def validarFechas(checkin,checkout):
    if formatearFecha(checkin) <= formatearFecha(checkout):
        return True
    else:
        return False

