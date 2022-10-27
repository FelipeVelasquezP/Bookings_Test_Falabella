from flask import Flask,jsonify,request
from utils.connection import Conector

app=Flask(__name__)

@app.route('/',methods=['GET'])
def getdata():
    return 'HOLA'


def exceptRequest(error):
    return "<h1>error</h1>"

if __name__=='__main__':
    app.register_error_handler(404,exceptRequest)
    app.run()