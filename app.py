from bson.objectid import ObjectId
from flask import Flask, request, Response
from bson import json_util
###Modulos propios
####Models
from models.wine import Wine
from models.client import Client
from models.restaurant import Resturant
####Conecciones
import network.coneccion as conect
app = Flask(__name__)
##/ Ruta principal
@app.route("/")
def hello():
    response = {
        'principal': 'Ruta principal'
    }
    return response
#########---------Wine-----------------------------------------------
@app.route("/vino/inserts", methods = ['POST'])
def wine_insert():
    wine_model = Wine(
        request.json['nombre'],request.json['tipo_uva'],
        request.json['anio'],request.json['pais'])
    col = conect.coleccion1('wine')
    col.insert_one({
        'nombre': wine_model.nombre, 
        'tipo_uva': wine_model.tipo_uva,
        'anio': wine_model.anio,
        'pais': wine_model.pais
    })
    response = {
        'nombre': wine_model.nombre, 
        'tipo_uva': wine_model.tipo_uva,
        'anio': wine_model.anio,
        'pais': wine_model.pais
    }
    return response

@app.route("/vino/delete", methods = ['POST'])
def wine_delete():
    id = request.json['id']
    col = conect.coleccion1('wine')
    resultado = col.delete_one(
        {
            '_id': ObjectId(id)
        }
    )
    response = {
        'id': id, 
        'delete_count': resultado.deleted_count
    }
    return response

@app.route("/vino/update", methods = ['POST'])
def wine_update():
    col = conect.coleccion1('wine')
    id = request.json['id']
    wine_model = Wine(
        request.json['nombre'],request.json['tipo_uva'],
        request.json['anio'],request.json['pais'])
    result = col.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": wine_model.nombre,
                "tipo_uva": wine_model.tipo_uva,
                "anio": wine_model.anio,
                "pais" : wine_model.pais
            }
        })
    response = {
        "id":str(id),
        "nombre": wine_model.nombre,
        "tipo_uva": wine_model.tipo_uva,
        "anio": wine_model.anio,
        "pais" : wine_model.pais
    }
    return response

@app.route("/vino/select", methods = ['GET','POST'])
def wine_select():
    col = conect.coleccion1('wine')
    resultado = col.find()
    d = json_util.dumps(resultado)
    return Response(d, mimetype="aplication/json")
    
#########--------------------------------------------------------
#########---------Client-----------------------------------------------
@app.route("/cliente/inserts", methods = ['POST'])
def client_insert():
    client_model = Client(
        request.json['nombre'],request.json['email'],
        request.json['telefono'],request.json['restaurant_link'])
    col = conect.coleccion1('client')
    col.insert_one({
        'nombre': client_model.nombre, 
        'email': client_model.email,
        'telefono': client_model.telefono,
        'restaurant_link': client_model.restaruants_link
    })
    response = {
        'nombre': client_model.nombre, 
        'email': client_model.email,
        'telefono': client_model.telefono,
        'restaurant_link': client_model.restaruants_link
    }
    return response

@app.route("/cliente/delete", methods = ['POST'])
def client_delete():
    id = request.json['id']
    col = conect.coleccion1('client')
    resultado = col.delete_one(
        {
            '_id': ObjectId(id)
        }
    )
    response = {
        'id': id, 
        'delete_count': resultado.deleted_count
    }
    return response

@app.route("/cliente/update", methods = ['POST'])
def client_update():
    col = conect.coleccion1('client')
    id = request.json['id']
    client_model = Client(
        request.json['nombre'],request.json['email'],
        request.json['telefono'],request.json['restaurant_link'])
    result = col.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
        'nombre': client_model.nombre, 
        'email': client_model.email,
        'telefono': client_model.telefono,
        'restaurant_link': client_model.restaruants_link
            }
        })
    response = {
        "id":str(id),
        'nombre': client_model.nombre, 
        'email': client_model.email,
        'telefono': client_model.telefono,
        'restaurant_link': client_model.restaruants_link
    }
    return response

@app.route("/cliente/select", methods = ['GET','POST'])
def client_select():
    col = conect.coleccion1('client')
    resultado = col.find()
    d = json_util.dumps(resultado)
    return Response(d, mimetype="aplication/json")
#########--------------------------------------------------------

#########--------------------------------------------------------
#########---------Restaurant-----------------------------------------------
@app.route("/restaurant/inserts", methods = ['POST'])
def restaurant_insert():
    restaurant_model = Resturant(
        request.json['nombre'],request.json['direccion'],
        request.json['encargado_reference'],request.json['wine_reference'])
    col = conect.coleccion1('restaurant')
    col.insert_one({
        'nombre': restaurant_model.nombre, 
        'direccion': restaurant_model.direccion,
        'encargado_reference': restaurant_model.encargado_reference,
        'wine_reference': restaurant_model.wine_reference
    })
    response = {
        'nombre': restaurant_model.nombre, 
        'direccion': restaurant_model.direccion,
        'encargado_reference': restaurant_model.encargado_reference,
        'wine_reference': restaurant_model.wine_reference
    }
    return response

@app.route("/restaurant/delete", methods = ['POST'])
def restaurant_delete():
    id = request.json['id']
    col = conect.coleccion1('restaurant')
    resultado = col.delete_one(
        {
            '_id': ObjectId(id)
        }
    )
    response = {
        'id': id, 
        'delete_count': resultado.deleted_count
    }
    return response

@app.route("/restaurant/update", methods = ['POST'])
def restaurant_update():
    col = conect.coleccion1('restaurant')
    id = request.json['id']
    restaurant_model = Resturant(
        request.json['nombre'],request.json['direccion'],
        request.json['encargado_reference'],request.json['wine_reference'])
    result = col.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
        'nombre': restaurant_model.nombre, 
        'direccion': restaurant_model.direccion,
        'encargado_reference': restaurant_model.encargado_reference,
        'wine_reference': restaurant_model.wine_reference
            }
        })
    response = {
        "id":str(id),
        'nombre': restaurant_model.nombre, 
        'direccion': restaurant_model.direccion,
        'encargado_reference': restaurant_model.encargado_reference,
        'wine_reference': restaurant_model.wine_reference
    }
    return response

@app.route("/restaurant/select", methods = ['GET','POST'])
def restaurant_select():
    col = conect.coleccion1('restaurant')
    resultado = col.find()
    d = json_util.dumps(resultado)
    return Response(d, mimetype="aplication/json")
    
#########--------------------------------------------------------
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': "Resource not found" + request.url,
        'status': 404
    }
    return message
if __name__ == '__main__':
    app.run(debug=True)