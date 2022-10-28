"""
Archivo: conecto.py
Descripción: Este es el lugar donde Flask se conecta con la base de datos en MYSQL y realiza acciones de quering
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""
#Se importa la bilbioteca para acceder a mysql
import pymysql

#Creadeciales de la base de datos
DBINFO = {
    'host' : "localhost",
    'user' : "root",
    'password': "1234",
    'database': "Bookings"
}

#Datos de configuracion para la conexión
TYPE_CURSOR =  {
  "Cursor": None,
  "SSCursor": pymysql.cursors.SSCursor,
  "DictCursor": pymysql.cursors.DictCursor,
  "SSDictCursor": pymysql.cursors.SSDictCursor
}

#La clase Conector tiene los atributos y metodos nesesarios para hacer querys a la base de datos
class Conector:

    #Contructor de la clase, recibe todas las credenciales nesesarias
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host # localhost
        self.user = user #user
        self.password = password #*****
        self.database = database # base de datos
        self.connection = None # es vacia porque se inicializa cuando se requiera

    # Metodo que crear la conexión entre a app y la base de datos
    def connect(self):
        #Se crea la conexión
        self.connection = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)

    # Metodo que ejecuta un query y retorna el resultado
    def execute_query(self, query, data=()): # Recibe el query y los datos formateados del query
        c = self.get_cursor() # se obtiene el cursor
        c.execute(query, data) # Se ejecua el query
        return c.fetchall() # Se retorna el query en forma de diccionario
    
    # Metodo que confirm un cambio en la base de dtos, se utilza para inserts y updates
    def commit_change(self):
        self.connection.commit() # se hace el commit para la conexión

    #Metodo que obtiene el cursor de la base de datos
    def get_cursor(self):
        return self.connection.cursor() # retorna el cursos
    
    #Metodo que cierra la conexión a la base de datos
    def close(self):
        self.connection.close()# cierra la conexión