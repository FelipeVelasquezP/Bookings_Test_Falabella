"""
Archivo: modeloHabitacion.py
Descripción: Este es el modelo para los Habitacion y contiene los metodos que se nesesitan para anejar su información
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""
#Se importan las librerias nesesarias
import sys
import datetime
from tkinter import TRUE
sys.path.append('../utils')

#Se importan las conexiones a la base de datos
from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

#Clase Hotel que coniene los metodos y atributos del mismo
class Habitacion:
    #Conructor de la clase, recibe el id del hotel
    def __init__(self,reserva):
        self.reserva=reserva

    """ Metodo que obtiene una habitción libre en un rango de fechas para un hotel
        @self: Objeto Reserva (si mismo)
        Retorna : None
    """
    def obtenerHabitacionLibre(self):
        #Sentenci SQL para obtener las habitaciones que no tienen registros de reservas(estan disponibles siempre)
        query = "SELECT idHabitacion FROM habitacion\
        WHERE Hotel_idHotel=%s and  idHabitacion NOT IN (SELECT Habitacion_idHabitacion FROM Reserva);"
        cc = Connection().getCursor("DictCursor")# Se crea la conexión
        r = cc.execute(query,(self.reserva.idHotel))# Se ejecuta el query con los valores dados
        cc.close()# se cierra la conexión
        if r: # Si no esta vacio
            self.reserva.habitacion= cc.fetchall()[0]['idHabitacion'] # se asigna la habitacion para la reserva
        else: # si esta vacio
            habitaciones=self.obtenerHabitacionesHotel() # se traen las habitaciones que tienen reservas para el hotel
            for habitacion in habitaciones: # se revisa por cda habitación cual esta libre
                self.validarDisponibilidad(habitacion['idHabitacion']) # Se valida si esta libre la habitacion
                if self.reserva.habitacion !=None: # Si se asigno una habitación
                    return #acaba el ciclo porque ya encontro una habitación
            self.reserva.habitacion=0 # en caso de que no indique la habitacion 0, haciendo referencia a ue no hay habitaciones disponibles



    """ Metodo que obtiene las habitaciones de un hotel que tienen reservas:
        @self: Objeto Reserva (si mismo)
        Retorna : json con los datos de las reservas
    """
    def obtenerHabitacionesHotel(self):
        #Query que retorna las habitaciones que tienen o han tenido reservas al mnos 1 vez
        query = "SELECT distinct idHabitacion FROM Reserva,Habitacion\
        WHERE Hotel_idHotel=%s and Habitacion_idHabitacion=idHabitacion"
        cc = Connection().getCursor("DictCursor")# Se crea la conexión
        r = cc.execute(query,(self.reserva.idHotel)) # se ejecuta el query con los valores dados
        cc.close() # se cierra la conexión
        if r: # si no esta vacio
            return cc.fetchall() # retornar las habitaciones en formato json
        else: # si esta vacio
            return [] # no hay habitaciones


    """ Metodo que valida si una habitación tiene disponibilidd en un rango de fechas:
        @self: Objeto Reserva (si mismo)
        Retorna : json con los datos de las reservas
    """
    def validarDisponibilidad(self,habitacion):
        #Query que obtiene las reservas de una habitacion
        query = "select checkin,checkout from Reserva where Habitacion_idHabitacion=%s"         
        cc = Connection().getCursor("DictCursor")# se crea la conexión
        r = cc.execute(query,(habitacion))#se ejecuta el query con los valores dados
        cc.close()# se cierra la conexión
        if r: # si la habitación tiene reservas
            aux=[] # avriable auxiliar para verificar si la habitación tiene disponliilidad
            for reserva in cc.fetchall(): # se itera cada una de las reservas
                #se fromatean las fechas a evaluar para poder operarlas con <> == =!
                checkin,checkout=self.formatearFecha(str(reserva['checkin'])),self.formatearFecha(str(reserva['checkout']))
                checkinDeseado,checkoutDeseado=self.formatearFecha(str(self.reserva.checkin)),self.formatearFecha(str(self.reserva.checkout))
                #se valida si las fechas estan entre la reserva
                if (checkinDeseado>=checkin and checkinDeseado<checkout) \
                or (checkoutDeseado>checkin and checkoutDeseado<checkout):
                    aux.append(False) # si el rango esta en las fechas, no se puede usar
                else:
                    aux.append(True) # si el rango esta en las fechas, si se puede usar
            #Validar si existio algun caso donde la habitación esta ocupada
            if False not in aux: # si esta libre
                self.reserva.habitacion=habitacion # Se asigna el id de la habitacion
        else:
            pass



    """ Metodo estatico que formatea un fecha de string a date():
        @self: String : fecha a castear
        Retorna : Date: fecha casteada
    """
    @staticmethod
    def formatearFecha(fecha):
        indices=fecha.split('-')# se hace un split ara obetner el dia mes y año
        return datetime.date(int(indices[0]),int(indices[1]), int(indices[2])) # se castea la fechaa