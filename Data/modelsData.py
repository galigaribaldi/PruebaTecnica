# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras as extras
import pandas as pd
from psycopg2.extensions import register_adapter, AsIs
import numpy as np
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
psycopg2.extensions.register_adapter(np.float64, psycopg2._psycopg.AsIs)
######Datos ordenados
####1.- Devuelve los datos, opcion 1 decimales, opcion 2 Enteros
####2.- Devuelve id de marca
####3.- Devuelve la etiqueta
###################Claves para la BD#####################
###################     StratApp30       #####################
class ModelsData():
    host = 'ec2-44-196-68-164.compute-1.amazonaws.com'
    database = 'ddaui1ic2hdida'
    user = 'nnckmgzasylosx'
    password = '99b170dfe60bb4771b0ac9edf19939df386bc88cf1222aa7fe69ce6446a4a254'
    
    def create_tables(self):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE estado(
                              esatado_id integer primary key,
                              nombre_enetidad character varying not null,
                              clave_entidad integer not null
                            );
                    """)
        cursor.execute("""CREATE TABLE municipio(
                                municipio_id integer primary key,
                                nombre_municipio character varying null,
                                nombre_ciudad character varying null,
                                clave_municipio integer not null,
                                clave_ciudad integer null,
                                esatado_id integer,
                                CONSTRAINT esatado_id_fk FOREIGN KEY (esatado_id)
                                REFERENCES estado (esatado_id)
                                );
                    """)
        cursor.execute("""CREATE TABLE colonia(
                            colonia_id integer primary key,
                            codigo_postal_asentamiento integer,
                            nombre_colonia character varying null,
                            tipo_asentamiento character varying null,
                            codigo_postal_administracion character varying,
                            clave_tipo_asentamiento integer not null,
                            asentamiento_id integer null,
                            zona_asentamiento character varying null,
                            esatado_id integer,
                            municipio_id integer,
                            CONSTRAINT esatado_id_fk FOREIGN KEY (esatado_id)
                                REFERENCES estado (esatado_id),
                            CONSTRAINT municipio_id_fk FOREIGN KEY (municipio_id)
                                REFERENCES municipio (municipio_id)            
                            );

                    """)                
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Creacion de tablas")

    def delete_Info_Tables(self):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        cursor.execute("""DELETE FROM colonia;
                       DELETE FROM municipio;
                       DELETE FROM estado;
                       """)       
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Borrar Info de  Tablas")

    def drop_Tables(self):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        cursor.execute("""DROP TABLE colonia;
                       DROP TABLE municipio;
                       DROP TABLE estado;
                       """)       
        conexion.commit()
        cursor.close()
        conexion.close()
    print("Borrar Tablas")        
    def selectEstado(self):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        cursor.execute("""SELECT * FROM estado
                       """)    
        datos = cursor.fetchall()   
        conexion.commit()
        cursor.close()
        conexion.close()
        print(datos)
        
    def insertEstado_batch(self,tuples):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        query = "INSERT INTO estado(esatado_id, nombre_enetidad,clave_entidad) VALUES (%s, %s, %s)"
        extras.execute_batch(cursor, query, tuples, page_size=1000)
        conexion.commit()
        cursor.close()
        conexion.close()
                      
    def insertMunicipio_batch(self,tuples):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        query = "INSERT INTO municipio(municipio_id,nombre_municipio,nombre_ciudad,clave_municipio,clave_ciudad,esatado_id) VALUES (%s, %s, %s,%s,%s,%s)"
        extras.execute_batch(cursor, query, tuples, page_size=1000)
        conexion.commit()
        cursor.close()
        conexion.close()                
    
    def insertColonia_batch(self,tuples):
        conexion = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conexion.cursor()
        query = """INSERT INTO colonia(colonia_id, codigo_postal_asentamiento,nombre_colonia,tipo_asentamiento,codigo_postal_administracion,clave_tipo_asentamiento,asentamiento_id,zona_asentamiento,esatado_id,municipio_id)
                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"""
        extras.execute_batch(cursor, query, tuples, page_size=1000)
        conexion.commit()
        cursor.close()
        conexion.close()                                