"""
Archivo: config.py
Descripción: Este es el lugar donde Flask pone ciertos valores de configuración 
            y también donde las extensiones pueden poner sus valores de configuración..
Autor: Luis Felipe Velasquez Puentes
Fecha: 27/10/22
"""

#Se agregan las librerias nesesarias
import os
#Se emapqueta tod la aplicación
basedir = os.path.abspath(os.path.dirname(__file__))

#Clase que tiene los valores de confihuración iniciales
class Config(object):
    #Valores de configuración
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')