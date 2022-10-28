"""
Archivo: modeloHotel.py
Descripción: Este es el modelo para los Hoteles y contiene los metodos que se nesesitan para anejar su información
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""
#Se importan las librerias nesesarias
import sys
from tkinter import TRUE
sys.path.append('../utils')

#Se importan las conexiones a la base de datos
from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

#Clase Hotel que coniene los metodos y atributos del mismo
class Hotel:
    #Conructor de la clase, recibe el id del hotel
    def __init__(self,id=None):
        self.id=id # id del hotel

    """ Metodo que verifica si un hotel existe en la BD:
        @self: Objeto Hotel (si mismo)
        Retorna : Booleano(si el hotel existe o no)
    """
    def verificarSiExiste(self):
        query = "select idHotel from Hotel where idHotel=%s"#Se inicializa el query
        cc = Connection().getCursor("DictCursor")#se crea la conexión a la BD
        r = cc.execute(query,(self.id)) # Se ejecuta el query cn los datos a evaluar
        cc.close() # se cierra la conexión
        if r: # si no esta vacia
            return True # El hotel existe
        else: 
            return False # el hotel no existe