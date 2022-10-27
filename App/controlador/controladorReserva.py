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
    checkin=data.get('checkin')
    checkout=data.get('checkout')
    if validarFechas(checkin,checkout):
        reserva=Reserva(checkin=checkin,checkout=checkout,usuario=data.get('idUsuario'),idHotel=data.get('idHotel'))
        reserva.obtenerHabitacionLibre()
        reserva=reserva.agregarReserva()
        return {'reservas':reserva,'DataProperties':"Success"}
    else:
        return jsonify({'reservas':[],'DataProperties':"Error","descripcion":"checkout debe ser mayor a checkin"})
        

@bp.route('/cancelarReserva',methods=['PUT'])
def cancelarReserva():
    data = request.get_json()
    reserva=Reserva(id=data.get('idReserva'))
    if reserva.verificarSiExiste():
        if reserva.cancelarReserva():
            return {'idReserva':reserva.id,'DataProperties':"Success"}
        else:
            return {'DataProperties':"Error"}
    else:
        return {'DataProperties':"Error","description":"La reserva no existe"}



@bp.route('/consultarReservas',methods=['GET'])
def consultarReservas():
    data = request.get_json()
    checkin=data.get('checkin')
    checkout=data.get('checkout')
    if validarFechas(checkin,checkout):
        reserva=Reserva(checkin=checkin,checkout=checkout,idHotel=data.get('idHotel'))
        reservas=reserva.conultarReservas()
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

