"""
Archivo: conecto.py
Descripción: Este es el lugar donde Flask se conecta con la base de datos en MYSQL y realiza acciones de uppdating and inserting
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
class Connection(object):
  _connection = None # es vacia porque se inicializa cuando se requiera

  #Contructor de la clase, recibe todas las credenciales nesesarias
  def __init__(self):
    self.host = DBINFO['host'] #ocalhost
    self.user = DBINFO['user'] #user
    self.password = DBINFO['password'] #*****
    self.database = DBINFO['database'] # base de datos
    #Se iniclializa y crea la conexión a la base de datos
    self.conn = pymysql.connect(
      host=self.host, 
      user=self.user, 
      password=self.password, 
      database=self.database
    )

  #Metodo que valia si la conexión exite
  def __new__(cls, *args, **kwargs):
    if cls._connection is None: # si no exite, cree una nueva conexion
      cls._connection = super(Connection, cls).__new__(cls) # crea una nueva conexión
    return cls._connection #retorna la nueva conexión

  #Metodo que verifica si la app esta conectada a la base de datos
  def connect(self):
    if not self.isOpen(): # Si esta abierta 
      self.conn.ping() # hacer una prueba de ping

  #metodo que cierra la conexión a la base de datos
  def close(self): 
    if self.isOpen(): # si esta abierta
      self.conn.close() # cerrar la conexion

  # Metodo que confirm un cambio en la base de dtos, se utilza para inserts y updates
  def commit(self):
    if self.isOpen(): # si esta abierta
      self.conn.commit() # hacer la confirmación

  #controla el paso de conexión entre la app y BD
  def rollblack(self):
    if self.isOpen():# si esta abierta
      self.conn.rollback() #controlar las conexiones
  
  # Metodo que retorna la conexión avierta
  def isOpen(self):
    return self.conn.open # retorna la conexión abierta

  #Metodo que obtiene el cursor de la base de datos
  def getCursor(self, c="Cursor"):
    if not self.isOpen():# si no esta abierta
      self.connect() #se conecta a la BD
    return self.conn.cursor(TYPE_CURSOR[c]) # retorna el cursor