import sys
from tkinter import TRUE
sys.path.append('../utils')

from app.utils.conector import Conector,DBINFO
from app.utils.connection import Connection

class Hotel:
    def __init__(self,id=None):
        self.id=id

    def verificarSiExiste(self):
        query = "select idHotel from Hotel where idHotel=%s"
        cc = Connection().getCursor("DictCursor")
        r = cc.execute(query,(self.id))
        cc.close()
        if r:
            return True
        else:
            return False