from flask import Flask
from flask import request, render_template, url_for,redirect
from flask import jsonify
##Modulos propios
from Data.modelsData import ModelsData
modelo = ModelsData()
app = Flask(__name__)
##Creamos nuestro primer decorador, lo que nos permite crear la ruta principal "/
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/api/estado/<int:opcion>")
def api_estado(opcion):
    if opcion==1:
        c = modelo.consultaEstado(opcion=opcion)
        return c
    if opcion==2:
        c = modelo.consultaEstado(opcion=opcion)
        print(c)
        print(type(c))
        return jsonify(c)
@app.route("/api/municipio/<int:opcion>")
def api_municipio(opcion):
    if opcion==1:
        c = modelo.consultaMunicipio(opcion=opcion)
        return c
    if opcion==2:
        c = modelo.consultaMunicipio(opcion=opcion)
        print(c)
        print(type(c))
        return jsonify(c)
@app.route("/api/colonia/<int:opcion>")
def api_colonia(opcion,busqueda):
    if opcion==1:
        c = modelo.consultaColonia(opcion=opcion)
        return c
    if opcion==2:
        c = modelo.consultaColonia(opcion=opcion)
        print(c)
        print(type(c))
        return jsonify(c)
@app.route("/api/coloniaBusqueda/<int:opcion>/<int:busqueda>")    
def api_colonia_busqueda(opcion,busqueda):
    if opcion==1:
        c = modelo.consultaColonia(opcion=opcion,busqueda=busqueda)
        return c
    if opcion==2:
        c = modelo.consultaColonia(opcion=opcion,busqueda=busqueda)
        print(type(c))
        return jsonify(c)  
  
@app.route("/api/coloniaBusquedaNombre/<int:opcion>/<string:busqueda>")    
def api_colonia_busqueda_nombre(opcion,busqueda):
    if opcion==1:
        c = modelo.consultaColonia(opcion=opcion,busquedaNombre=busqueda)
        return c
    if opcion==2:
        c = modelo.consultaColonia(opcion=opcion,busquedaNombre=busqueda)
        print(type(c))
        return jsonify(c)        
if __name__ == "__main__":
    app.run(debug=True,port=5003)