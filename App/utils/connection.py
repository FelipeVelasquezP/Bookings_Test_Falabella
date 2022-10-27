from flask_mysqldb import MySQL

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234'
    MYSQL_DB = 'prueba2'

    



config = {
    'development':DevelopmentConfig
}