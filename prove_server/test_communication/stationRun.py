'''
Created on 16/mag/2015
@author: Riccardo

This method is used to run the Flask application on the station side.
The station must contain a server in order to listen to commands from 
the "true" server. 

'''

from flask import Flask, request, Request
from flask.templating import render_template
from stationFunctions import decode_data, encode_data

app = Flask ('test_communication')

@app.route('/')
def index():
    return render_template('indexStation.html')

@app.route('/post', methods = ['POST'])
def post():
    return render_template('response.html')
    #d = Request.form['k1']
    #j_data = Request.get_json()
    #d = decode_data(j_data)
    d = 123
    print d
    
if __name__ == '__main__':
    app.run ('localhost', port = 8000)
    