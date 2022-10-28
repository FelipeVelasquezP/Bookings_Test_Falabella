from ast import Or
import sys
import datetime
from tkinter import TRUE
sys.path.append('../utils')
from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

class Reserva:
    def __init__(self,id=None,idHotel=None, checkin=None, checkout=None, fechaReserva=None, estadoReserva=None, usuario=None, habitacion=None):
        self.fechaReserva=fechaReserva
        self.id=id
        self.checkin=checkin
        self.checkout=checkout
        self.estadoReserva=estadoReserva
        self.usuario=usuario
        self.habitacion=habitacion
        self.idHotel=idHotel

    def agregarReserva(self):
        if self.habitacion==0:
            return {"Error":"No hay habitaciones disponibles para estas fechas"}
        query = "insert into Reserva values(null,%s,%s,utc_date(),'reservado',%s,%s);"
        c = Connection()
        cs = c.getCursor()
        r = cs.execute(query, (self.checkin, self.checkout, self.usuario, self.habitacion))
        if r:
            self.id = cs.lastrowid
            c.commit()
        c.close()
        return {"idReserva:":self.id,"idHabitacion":self.habitacion}


    def cancelarReserva(self):
        sql =  f"update Reserva set estadoReserva='cancelado',checkin='1677-09-21',checkout='1677-09-21' where idReserva={self.id};"
        conn = Conector(DBINFO['host'], DBINFO['user'],
                            DBINFO['password'], DBINFO['database'])
        conn.connect()
        conn.execute_query(sql)
        conn.commit_change()
        conn.close()
        return True 

    def conultarReservas(self):
        query = "select idReserva,checkin,checkout,fechaReserva,idHabitacion,nombreHotel,emailUsuario \
                 from Reserva,Usuario,Habitacion,Hotel where idHabitacion=Habitacion_idHabitacion and \
                 idHotel=Hotel_idHotel and idUsuario=Usuario_idUsuario and estadoReserva='reservado' and\
                 checkin between %s and %s and idHotel=%s;"

        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.checkin,self.checkout,self.idHotel))
        cc.close()
        if r:
            return cc.fetchall()


    def obtenerHabitacionLibre(self):
        query = "SELECT idHabitacion FROM habitacion\
        WHERE Hotel_idHotel=%s and  idHabitacion NOT IN (SELECT Habitacion_idHabitacion FROM Reserva);"
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.idHotel))
        cc.close()
        if r:
            self.habitacion= cc.fetchall()[0]['idHabitacion']
        else:
            habitaciones=self.obtenerHabitacionesHotel()
            for habitacion in habitaciones:
                self.validarDisponibilidad(habitacion['idHabitacion'])
                if self.habitacion !=None:
                    return
            self.habitacion=0



    def obtenerHabitacionesHotel(self):
        query = "SELECT distinct idHabitacion FROM Reserva,Habitacion\
        WHERE Hotel_idHotel=%s and Habitacion_idHabitacion=idHabitacion"
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.idHotel))
        cc.close()
        if r:
            return cc.fetchall()
        else:
            return []



    def validarDisponibilidad(self,habitacion):
        query = "select checkin,checkout from Reserva where Habitacion_idHabitacion=%s"         
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(habitacion))
        cc.close()
        if r:
            aux=[]
            for reserva in cc.fetchall():
                checkin,checkout=self.formatearFecha(str(reserva['checkin'])),self.formatearFecha(str(reserva['checkout']))
                checkinDeseado,checkoutDeseado=self.formatearFecha(str(self.checkin)),self.formatearFecha(str(self.checkout))
                if (checkinDeseado>=checkin and checkinDeseado<checkout) \
                or (checkoutDeseado>checkin and checkoutDeseado<checkout):
                    aux.append(False)
                else:
                    aux.append(True)
            if False not in aux:
                self.habitacion=habitacion
        else:
            pass


    def verificarSiExiste(self):
        query = "select idReserva from Reserva where idReserva=%s"
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.id))
        cc.close()
        if r:
            return True
        else:
            return False

    @staticmethod
    def formatearFecha(fecha):
        indices=fecha.split('-')
        return datetime.date(int(indices[0]),int(indices[1]), int(indices[2])) 