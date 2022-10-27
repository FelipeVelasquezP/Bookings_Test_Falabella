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
    def conultarReservas(checkin,checkout):
        query = "SELECT * from Reserva"
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query)
        cc.close()
        if r:
            return cc.fetchall()