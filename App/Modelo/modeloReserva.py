"""
Archivo: modeloReserva.py
Descripción: Este es el modelo para los Reservas y contiene los metodos que se nesesitan para anejar su información
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""
#Se importan las librerias nesesarias
from ast import Or
import sys
import datetime
from tkinter import TRUE
sys.path.append('../utils')

#Se importan las conexiones a la base de datos
from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

#Clase Reserva que coniene los metodos y atributos del mismo
class Reserva:
    #Conructor de la clase, recibe los datos de la entidad Reserva de la BD
    def __init__(self,id=None,idHotel=None, checkin=None, checkout=None, fechaReserva=None, estadoReserva=None, usuario=None, habitacion=None):
        self.fechaReserva=fechaReserva # fechareserva
        self.id=id # id de la reserva
        self.checkin=checkin # checkin de la reserva 
        self.checkout=checkout # checkout de la reserva
        self.estadoReserva=estadoReserva #estado de la reserva
        self.usuario=usuario # usuario de la reserva
        self.habitacion=habitacion #habitacion de de la reserva
        self.idHotel=idHotel #hotel de la reserva


    """ Metodo que agrega una reserva dado un hotel, usuario y rango de fechas:
        @self: Objeto Reserva (si mismo)
        Retorna : Json = Habitacion asignada y el id de la reserva
    """
    def agregarReserva(self):
        #cuando el id de la habitacion es 0, quere decir que no hay habitaciones disponibles
        if self.habitacion==0:
            return {"Error":"No hay habitaciones disponibles para estas fechas"} # se retorna la advertencia
        query = "insert into Reserva values(null,%s,%s,utc_date(),'reservado',%s,%s);" # Se crea el insert para crear la reserva
        c = Connection() # se crea la conexión
        cs = c.getCursor() # se obtiene el cursor
        r = cs.execute(query, (self.checkin, self.checkout, self.usuario, self.habitacion)) # Se ejcuta el nsert con los valores dados
        if r: # si fue exitoso
            self.id = cs.lastrowid # se asina el id de la reserva
            c.commit() # se confirma el camvio en la bd
        c.close() # se sierra la conexión
        return {"idReserva:":self.id,"idHabitacion":self.habitacion} #se retornan los datos nesesarios


    """ Metodo que cancela una reserva dato el id de la reserva:
        @self: Objeto Reserva (si mismo)
        Retorna : Booleano si se atualizo la reserva 
    """
    def cancelarReserva(self):
        #Sencia SQL ara actualizar la reserva
        sql =  f"update Reserva set estadoReserva='cancelado',checkin='1677-09-21',checkout='1677-09-21'\
                 where idReserva={self.id};"
        #Se crea la conexión
        conn = Conector(DBINFO['host'], DBINFO['user'],
                            DBINFO['password'], DBINFO['database'])
        conn.connect() # Se conecta a la BD
        conn.execute_query(sql) # Se ejecuta la sentencia
        conn.commit_change() # Se confiman los cambios en la BD 
        conn.close() # Se cierra la conexión
        return True # se retorna la confirmación


    """ Metodo que  las reserva dato un hotel y un rango de fechas:
        @self: Objeto Reserva (si mismo)
        Retorna : json con los datos de las reservas
    """
    def conultarReservas(self):
        #Sentencia SQL que tiene el query a realizar 
        query = "select idReserva,checkin,checkout,fechaReserva,idHabitacion,nombreHotel,emailUsuario \
                 from Reserva,Usuario,Habitacion,Hotel where idHabitacion=Habitacion_idHabitacion and \
                 idHotel=Hotel_idHotel and idUsuario=Usuario_idUsuario and estadoReserva='reservado' and\
                 checkin between %s and %s and idHotel=%s;"
        #Se crea la conexión y se trae el cursor
        cc = Connection().getCursor("DictCursor")
        #Se ejecuta el Query con los datos a validar
        r = cc.execute(query,(self.checkin,self.checkout,self.idHotel))
        cc.close() # se cierra la conexión
        if r: # si no esta vacio
            return cc.fetchall() # retorne las reservas en formato json


    """ Metodo que verifica si una Reserva existe en la BD:
        @self: Objeto Reserva (si mismo)
        Retorna : Booleano(si la Reserva existe o no)
    """
    def verificarSiExiste(self):
        query = "select idReserva from Reserva where idReserva=%s"#Se inicializa el query
        cc = Connection().getCursor("DictCursor")#se crea la conexión a la BD
        r = cc.execute(query,(self.id))# Se ejecuta el query cn los datos a evaluar
        cc.close() # se cierra la conexión
        if r: # si no esta vacia
            return True # La reserva existe
        else:
            return False # La reserva no existe