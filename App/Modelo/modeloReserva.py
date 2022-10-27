import sys
sys.path.append('../utils')

from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

class Reserva:
    def __init__(self,id=None, checkin=None, checkout=None, fechaReserva=None, estadoReserva=None, usuario=None, habitacion=None):
        self.fechaReserva=fechaReserva
        self.id=id
        self.checkin=checkin
        self.checkout=checkout
        self.estadoReserva=estadoReserva
        self.usuario=usuario
        self.habitacion=habitacion

    def agregarReserva(self):
        return {}


    def cancelarReserva(self):
        return {}

    @staticmethod
    def conultarReservas(checkin,checkout,idHotel):
        query = "select idReserva,checkin,checkout,fechaReserva,idHabitacion,nombreHotel,emailUsuario \
                 from Reserva,Usuario,Habitacion,Hotel where idHabitacion=Habitacion_idHabitacion and \
                 idHotel=Hotel_idHotel and idUsuario=Usuario_idUsuario and estadoReserva='reservado' and\
                 checkin between %s and %s and checkout between %s and %s and idHotel=%s;"
                 
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(checkin,checkout,checkin,checkout,idHotel))
        cc.close()
        if r:
            return cc.fetchall()