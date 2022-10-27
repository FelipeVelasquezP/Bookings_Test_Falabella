import sys
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
        query = "insert into Reserva values(null,%s,%s,utc_date(),'reservado',%s,%s);"
        c = Connection()
        cs = c.getCursor()
        r = cs.execute(query, (self.checkin, self.checkout, self.usuario, self.habitacion))
        if r:
            self.id = cs.lastrowid
            c.commit()
        c.close()
        print(self.id)
        return {"idReserva:":self.id,"idHabitacion":self.habitacion}


    def cancelarReserva(self):
        sql =  f"update Reserva set estadoReserva='cancelado',checkin='0000-0-00',checkout='0000-0-00' where idReserva={self.id};"
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
                 checkin between %s and %s and checkout between %s and %s and idHotel=%s;"

        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.checkin,self.checkout,self.checkin,self.checkout,self.idHotel))
        cc.close()
        if r:
            return cc.fetchall()


    def obtenerHabitacionLibre(self):
        query = "select  idHabitacion from Reserva,Habitacion \
				where ((%s not between checkin and date_sub(checkout,interval 1 DAY))\
				and   (%s not between date_sub(checkin,interval 1 DAY) and checkout)\
                and idHabitacion=Habitacion_idHabitacion and Hotel_idHotel=%s)\
                or (idHabitacion!=Habitacion_idHabitacion and Hotel_idHotel=%s) limit 1;"
                 
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.checkin,self.checkout,self.idHotel,self.idHotel))
        cc.close()
        if r:
            self.habitacion= cc.fetchall()[0]['idHabitacion']

    def verificarSiExiste(self):
        query = "select idReserva from Reserva where idReserva=%s"
                 
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.id))
        cc.close()
        if r:
            return True
        else:
            return False