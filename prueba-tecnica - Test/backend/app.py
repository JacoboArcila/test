from typing import List
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from flask import Flask, request, jsonify #importo lo que necesito
import db #importo db para llamar la funcion de crear tabla
import productos #importo productos para las funciones GET, POST

app = Flask(__name__)



db.crear_tabla()

def conexion_auxiliar(): #Funcion auxiliar para la conexion de las peticiones
    return sqlite3.connect('Mercado.db')

#GET = LISTAR TODOS LOS PRODUCTOS
@app.route('/productos', methods = ['GET'])

def get_productos():

    conexion = conexion_auxiliar()
    listar = productos.listar_productos(conexion)
    conexion.close()
    return jsonify(listar)

       
#GET - PRODUCTO POR ID
@app.route('/productos/<int:producto_id>', methods = ['GET'])

def buscar_productos(producto_id):

    conexion = conexion_auxiliar()
    buscar = productos.buscar_producto(conexion, producto_id)
    conexion.close()

    if buscar:

        return jsonify(buscar)
    
    else:

        return jsonify({'Error': 'Producto no encontrado'})



#POST - AGREGAR PRODUCTO
@app.route('/productos', methods = ['POST'])

def agg_producto():

    data = request.get_json()
    print(data)
    conexion = conexion_auxiliar()
    mensaje = productos.agregar_producto(conexion, data['nombre'], data['precio'])
    conexion.close()

    return jsonify({'Mensaje': mensaje})
