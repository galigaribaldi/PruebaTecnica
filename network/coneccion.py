from pymongo import MongoClient

def conecccion(database_name):
    client = MongoClient('mongodb+srv://user1:user1@cluster0.kkxed.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
    db = client[database_name]
    return db

def coleccion1(nombre_coleccion):
    c = conecccion('prueba')
    col = c[nombre_coleccion]
    return col

def insert(diccionario):
    
    pass