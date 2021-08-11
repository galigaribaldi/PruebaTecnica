from flask import Flask
##Importamos la librería Flask
from flask import request, render_template, url_for,redirect
from flask import jsonify
##
app = Flask(__name__)
##Creamos nuestro primer decorador, lo que nos permite crear la ruta principal "/
@app.route("/")
def hello():
    ##Le decimos a nuestra función que retorne "Hola mundo"
    return render_template("index.html")

@app.route("/api")
def api():
    return "API"
if __name__ == "__main__":
    app.run(debug=True,port=5003)