"""
Archivo: controladorReserva.py
Descripción: Este es el controlador para las acciones de las reservas, en este codigo se encunetran
              el redireccionamiento de las rutas y el contro de los modelos creaos
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""

#Se importan los modelos
from app.modelo.modeloReserva import Reserva
from app.modelo.modeloHotel import Hotel
from app.modelo.modeloUsuario import Usuario
from app.modelo.modeloHabitacion import Habitacion

#Se importan las bibliotecas nesesarias
from app.controlador import bp
from flask import Flask,jsonify,request
import datetime

#Json que contiene algunos errores que se retornan cuando hay algun tipo de excepción
errores={
    "400": {'codigoError':400,'DataProperties':"Error","description":"Eror en Fechas(checkin menor a checkout o checkin menor a checkin)"},
    "401": {'codigoError':401,'DataProperties':"Error","description":"El Hotel, Usuario o Reserva no existen"},
    "402": {'codigoError':402,'DataProperties':"Error","description":"Accion no realizada"}
}

""" Función que tiene direccion raiz (funciona como testing)
    @RequestType: GET
    Retorna : String
"""
@bp.route('/',methods=['GET'])
def main():
    return 'Bienvenido a la API REST de Bookings Falabella'


""" Función que tiene direccion para crear una reserva dado u uduario, hoel y rango de fechas
    @RequestType: POST
    Retorna : JSON que contiene la habitacion asignad ay el idReserva
"""
@bp.route('/crearReserva',methods=['POST'])
def crearReserva():
    data = request.get_json()# Se obtiene los datos de la petición
    #Se formatean las fechas en date() para poder oparalas 
    checkin,checkout,usuario,hotel=data.get('checkin'),data.get('checkout'),\
                                   data.get('idUsuario'),data.get('idHotel')
    #Se crea el objeto de Rerserva
    reserva=Reserva(checkin=checkin,checkout=checkout,usuario=usuario,idHotel=hotel)
    #Validar si el usuario y el hotel existen
    if Usuario(id=usuario).verificarSiExiste() and Hotel(id=hotel).verificarSiExiste():# si existen
        #Calidar si las fechas se enviaron correctaamente(checkin< choecout y fechadeseada>checjin)
        if validarFechas(checkin,checkout) and (formatearFecha(checkin) > datetime.date.today()):# si cumple
            Habitacion(reserva).obtenerHabitacionLibre() # Se obtiene la habitación que este libre en el hoteñ
            reserva=reserva.agregarReserva() # se inserta la reserva en la base de datos
            return {'reserva':reserva,'DataProperties':"Success"} # Se retorna el mensaje de exito
        else: # si no cumle las fechas retorne el error 400
            return errores["400"]
    return errores["401"] #si no existen retornar el error 401


""" Función que tiene direccion para cancelar una reserva dado el id de la reserva
    @RequestType: PUT
    Retorna : JSON que indica si se actualizo la reserva
"""
@bp.route('/cancelarReserva',methods=['PUT'])
def cancelarReserva():
    data = request.get_json()# Se obtiene los datos de la petición
    reserva=Reserva(id=data.get('idReserva'))# secrea el objeto de la reserva
    if reserva.verificarSiExiste(): # Se valida si la reserva existe
        if reserva.cancelarReserva(): # Se cancela la reserva 
            return {'idReserva':reserva.id,'DataProperties':"Success"} # se indica que la reserva se actualiza
        else:
            return errores["402"] # si fallo retorna el error 402
    else:
        return errores["401"] # si no existe retorna el error 401




""" Función que tiene direccion para conultar reservas dado un hotel y rango de fechas
    @RequestType: GET
    Retorna : JSON que contiene reservas, datos de htel y del usuario
"""
@bp.route('/consultarReservas',methods=['GET'])
def consultarReservas():
    data = request.get_json()# Se obtiene los datos de la petición
    checkin,checkout=data.get('checkin'),data.get('checkout') # fechas colicitadas
    hotel=data.get('idHotel') # Se crea el objeto de hoteñ
    if Hotel(id=hotel).verificarSiExiste(): #si el hotel existe
        if validarFechas(checkin,checkout): # valida si fecha1<fecha2
            reserva=Reserva(checkin=checkin,checkout=checkout,idHotel=hotel)# crea el objeto reserva
            reservas=reserva.conultarReservas()# realiza el query con los parametros dados
            return jsonify({'reservas':reservas,'DataProperties':"Success"})# retorna el resultad exitoso
        else:
            return errores["400"] # retorna error en las fechas
    else:
        return errores["401"] #retorna que el otel no existe
    


#función que formatea un string en fecha
def formatearFecha(fecha):
    indices=fecha.split('-')#obtiene los indices de la fecha
    #retorna la fecha en formatoo date()
    return datetime.date(int(indices[0]),int(indices[1]), int(indices[2])) 
#Función que valida si una fecha es mayor a otra
def validarFechas(checkin,checkout):
    #validar si fecha1 es menor o igual a fecha 2
    if formatearFecha(checkin) <= formatearFecha(checkout):
        return True #si es
    else:
        return False # no es