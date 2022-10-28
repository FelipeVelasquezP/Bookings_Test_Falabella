from app.modelo.modeloReserva import Reserva
from app.modelo.modeloHotel import Hotel
from app.modelo.modeloUsuario import Usuario
from app.controlador import bp
from flask import Flask,jsonify,request
import datetime


errores={
    "400": {'codigoError':400,'DataProperties':"Error","description":"Eror en Fechas(checkin menor a checkout o checkin menor a checkin)"}
    "401": {'codigoError':401,'DataProperties':"Error","description":"El Hotel, Usuario o Reserva no existen"}      
    "402": {'codigoError':402,'DataProperties':"Error","description":"Accion no realizada"}
}


@bp.route('/',methods=['GET'])
def main():
    return 'Bienvenido a la API REST de Bookings Falabella'



@bp.route('/crearReserva',methods=['POST'])
def crearReserva():
    data = request.get_json()
    checkin,checkout,usuario,hotel=data.get('checkin'),data.get('checkout'),\
                                   data.get('idUsuario'),data.get('idHotel')
    reserva=Reserva(checkin=checkin,checkout=checkout,usuario=usuario,idHotel=hotel)
    if Usuario(id=usuario).verificarSiExiste() and Hotel(id=hotel).verificarSiExiste():
        if validarFechas(checkin,checkout) and (formatearFecha(checkin) > datetime.date.today()):
            reserva.obtenerHabitacionLibre()
            reserva=reserva.agregarReserva()
            return {'reserva':reserva,'DataProperties':"Success"}
        else:
            return errores["400"]
    return errores["401"]



@bp.route('/cancelarReserva',methods=['PUT'])
def cancelarReserva():
    data = request.get_json()
    reserva=Reserva(id=data.get('idReserva'))
    if reserva.verificarSiExiste():
        if reserva.cancelarReserva():
            return {'idReserva':reserva.id,'DataProperties':"Success"}
        else:
            return errores["402"]
    else:
        return errores["401"]




@bp.route('/consultarReservas',methods=['GET'])
def consultarReservas():
    data = request.get_json()
    checkin,checkout=data.get('checkin'),data.get('checkout')
    hotel=data.get('idHotel')
    if Hotel(id=hotel).verificarSiExiste():
        if validarFechas(checkin,checkout):
            reserva=Reserva(checkin=checkin,checkout=checkout,idHotel=hotel)
            reservas=reserva.conultarReservas()
            return jsonify({'reservas':reservas,'DataProperties':"Success"})
        else:
            return errores["400"]
    else:
        return errores["402"]       
    



def formatearFecha(fecha):
    indices=fecha.split('-')
    return datetime.date(int(indices[0]),int(indices[1]), int(indices[2])) 
def validarFechas(checkin,checkout):
    if formatearFecha(checkin) <= formatearFecha(checkout):
        return True
    else:
        return False