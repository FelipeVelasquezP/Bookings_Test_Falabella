"""
Archivo: modeloUsuario.py
Descripción: Este es el modelo para los Usuario y contiene los metodos que se nesesitan para anejar su información
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

#Clase Usuario que coniene los metodos y atributos del mismo
class Usuario:
    #Conructor de la clase, recibe el id del usuario
    def __init__(self,id=None):
        self.id=id #id del usuario

    """ Metodo que verifica si un Usuario existe en la BD:
        @self: Objeto Usuario (si mismo)
        Retorna : Booleano(si el Usuario existe o no)
    """
    def verificarSiExiste(self):
        query = "select idusuario from Usuario where idUsuario=%s"#Se inicializa el query
        cc = Connection().getCursor("DictCursor")#se crea la conexión a la BD
        r = cc.execute(query,(self.id))# Se ejecuta el query cn los datos a evaluar
        cc.close()# se cierra la conexión
        if r:#si no esta vacia
            return True # El usuario existe
        else:
            return False # El usuario no existe