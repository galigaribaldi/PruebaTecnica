# PruebaTecnica

Este repositorio contiene el código solciitado como pueba técnica, a continuación se explica a mayor detalle como es que está compuesto:

* Archivo **app.py**: Este Archivo es el que hace correr y funcionar la aplicación web, mas adelante se detalla de mejor manera, los archivos necesarios para correr la aplicación web. Las rutas principales se describen a continuación

  * Hello **( / )**: La ruta principal, la cual lleva a un template sencillo 

    ```python
    @app.route("/")
    def hello():
        return render_template("index.html")
    ```
    
  * Api de Estado **( /api/estado/<int:opcion> )**: La cual nos trae la consulta de todos lso datos del estado:

    ```python
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
    ```
    
    
    
  * Api de Municipio **( /api/municipio/<int:opcion> )**: La cual nos trae la consulta de todos lso datos del Municipio:

    ```python
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
    ```
    
  * APi de Colonia **/api/coloniaBusqueda/<int:opcion>/<int:busqueda>**: La cual nos trae la consulta de las colonias por búsqueda de Codigo postal:

    ```python
    @app.route("/api/coloniaBusqueda/<int:opcion>/<int:busqueda>")    
    def api_colonia_busqueda(opcion,busqueda):
        if opcion==1:
            c = modelo.consultaColonia(opcion=opcion,busqueda=busqueda)
            return c
        if opcion==2:
            c = modelo.consultaColonia(opcion=opcion,busqueda=busqueda)
            print(type(c))
            return jsonify(c) 
    ```

  * APi de Colonia **/api/coloniaBusquedaNombre/<int:opcion>/<string:busqueda>**: La cual nos trae la consulta de las colonias por búsqueda de su nombre:

    ```python
    @app.route("/api/coloniaBusquedaNombre/<int:opcion>/<string:busqueda>")    
    def api_colonia_busqueda_nombre(opcion,busqueda):
        if opcion==1:
            c = modelo.consultaColonia(opcion=opcion,busquedaNombre=busqueda)
            return c
        if opcion==2:
            c = modelo.consultaColonia(opcion=opcion,busquedaNombre=busqueda)
            print(type(c))
            return jsonify(c)   
    ```

    

* Archivo **lector.py**: En este archivo se detalla la lectura y transformación de los datos, para ello se utiliza la librería *pandas*, la que nos ayuda a dividir el archivo en subparte y transformarla a tuplas.

  De la misma forma para la transformación de los datos a tuplas, se usaron listas por comprensión, las cuales resultaron ser útiles, ya que se cargan en batch de 100 datos

  * ```python
    from modelsData import ModelsData
    import pandas as pd
    def CargaDatos():
        xls = pd.ExcelFile("Jalisco.xls")
        Carga = xls.parse('Jalisco')
        Carga = Carga.fillna(0)
        ###Colonia
        codigo_postal_colonia = (Carga['d_codigo'])
        nombre_colonia = (Carga['d_asenta'])
        tipo_asentamiento_colonia = (Carga['d_tipo_asenta'])
        codigo_postal_admin_colonia = (Carga['d_CP'])
        clave_asentamiento_colonia = (Carga['c_tipo_asenta'])
        id_asentamiento_colonia = (Carga['id_asenta_cpcons'])
        zona_colonia = (Carga['d_zona'])
        ###municipio
        nombre_municipio = (Carga['D_mnpio'])
        nombre_ciudad_municipio = (Carga['d_ciudad'])
        clave_municipio = (Carga['c_mnpio'])
        clave_ciudad_municipio = (Carga['c_cve_ciudad'])
        ###Estado
        nombre_estado = (Carga['d_estado'])
        clave_estado = (Carga['c_estado'])
        inicial =0;final=99;tam = len(nombre_estado)
        carga = ModelsData()
        print(tam)
        while tam >100:
            ###generacion de tuplas para  estado
            tuplaEstado = tuple([tuple([int(i),nombre_estado[i],int(clave_estado[i])]) for i in range(inicial, final)])
            ###Generacion de Municipio
            tuplaMunicipio = tuple([tuple([int(i),nombre_municipio[i],nombre_ciudad_municipio[i], int(clave_municipio[i]),int(clave_ciudad_municipio[i]), int(i)]) for i in range(inicial, final)])
            ###Generacion de Colonia
            tuplaColonia = tuple([tuple([int(i),int(codigo_postal_colonia[i]),nombre_colonia[i], tipo_asentamiento_colonia[i],int(codigo_postal_admin_colonia[i]), int(clave_asentamiento_colonia[i]),int(id_asentamiento_colonia[i]),zona_colonia[i],int(i),int(i)]) for i in range(inicial, final)])
            inicial = inicial+99
            final = final+99
            tam = tam-99
            carga.insertEstado_batch(tuplaEstado)
            print("Cargando Encuestado: ", len(tuplaEstado))
            carga.insertMunicipio_batch(tuplaMunicipio)
            print("Cargando Municipio: ", len(tuplaMunicipio))        
            carga.insertColonia_batch(tuplaColonia)
            print("Cargando Colonia: ", len(tuplaColonia))        
        if tam<=99:
            tuplaEstado = tuple([tuple([int(i),nombre_estado[i],int(clave_estado[i])]) for i in range(inicial, tam)])
            ###Generacion de Municipio
            tuplaMunicipio = tuple([tuple([int(i),nombre_municipio[i],nombre_ciudad_municipio[i], int(clave_municipio[i]),int(clave_ciudad_municipio[i]), int(i)]) for i in range(inicial, tam)])
            ###Generacion de Colonia
            tuplaColonia = tuple([tuple([int(i),int(codigo_postal_colonia[i]),nombre_colonia[i], tipo_asentamiento_colonia[i],int(codigo_postal_admin_colonia[i]), int(clave_asentamiento_colonia[i]),int(id_asentamiento_colonia[i]),zona_colonia[i],int(i),int(i)]) for i in range(inicial, tam)])
            carga.insertEstado_batch(tuplaEstado)
            print("Cargando Encuestado: ", len(tuplaEstado))
            carga.insertMunicipio_batch(tuplaMunicipio)
            print("Cargando Municipio: ", len(tuplaMunicipio))        
            carga.insertColonia_batch(tuplaColonia)
            print("Cargando Colonia: ", len(tuplaColonia))
    ```
    
    

* Archivo **modelsData.py**: Este archivo es donde se encuentran las definiciones de todas las operaciones de:

  * Creación de tablas

  * Borrado de tablas

  * Inserción de registros pro Batch (100 registros)

  * Consultas

  * ```python
    # -*- coding: utf-8 -*-
    import psycopg2
    import psycopg2.extras as extras
    import pandas as pd
    from psycopg2.extensions import register_adapter, AsIs
    import numpy as np
    psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
    psycopg2.extensions.register_adapter(np.float64, psycopg2._psycopg.AsIs)
    
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
        
        def consultaEstado(self,*args, opcion=1):
            query = """SELECT * FROM estado order by esatado_id desc;"""
            datos = pd.read_sql(query, con=psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password))
            if len(args) >0:
                parametros = args[0]
                datos = datos.sort_values(by = parametros, ascending=False)
            if opcion == 3:
                return datos
            if opcion ==1:
                diccionario = datos.to_json()
                return diccionario
            if opcion ==2:
                diccionario = {"encuestado_id":datos["esatado_id"].to_list(),
                               "nombre_entidad":datos["nombre_enetidad"].to_list(),"clave_entidad":datos["clave_entidad"].to_list()}
                return diccionario
            
        def consultaMunicipio(self,*args, opcion=1):
            query = """SELECT * FROM municipio order by esatado_id desc;"""
            datos = pd.read_sql(query, con=psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password))
            if len(args) >0:
                parametros = args[0]
                datos = datos.sort_values(by = parametros, ascending=False)
            if opcion == 3:
                return datos
            if opcion ==1:
                diccionario = datos.to_json()
                return diccionario
            if opcion ==2:
                diccionario = {"municipio_id":datos["municipio_id"].to_list(),
                               "nombre_municipio":datos["nombre_municipio"].to_list(),
                               "nombre_ciudad":datos["nombre_ciudad"].to_list(),
                               "clave_municipio":datos["clave_municipio"].to_list(),
                               "esatado_id":datos["esatado_id"].to_list()
                               }
                return diccionario
        
        def consultaColonia(self,*args, opcion=1,busqueda=False, busquedaNombre=False):
            query = """SELECT * FROM colonia order by esatado_id desc;"""
            datos = pd.read_sql(query, con=psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password))
            if len(args) >0:
                parametros = args[0]
                datos = datos.sort_values(by = parametros, ascending=False)
            if opcion == 3:
                return datos
            if opcion ==1:
                if type(busqueda) == int:
                    diccionario = datos[datos["codigo_postal_asentamiento"] == busqueda]
                    diccionario = diccionario.to_json()
                    return diccionario
                if type(busquedaNombre) == str:
                    diccionario = datos[datos["nombre_colonia"] == busquedaNombre]
                    diccionario = diccionario.to_json()
                    return diccionario            
                diccionario = datos.to_json()
                return diccionario
            if opcion ==2:
                if type(busqueda) == int:
                    diccionario = datos[datos["codigo_postal_asentamiento"] == busqueda]
                    print()
                    diccionario = {"colonia_id":diccionario["colonia_id"].to_list(),
                               "codigo_postal_asentamiento":diccionario["codigo_postal_asentamiento"].to_list(),
                               "nombre_colonia":diccionario["nombre_colonia"].to_list(),
                               "tipo_asentamiento":diccionario["tipo_asentamiento"].to_list(),
                               "codigo_postal_administracion":diccionario["codigo_postal_administracion"].to_list(),
                               "clave_tipo_asentamiento":diccionario["clave_tipo_asentamiento"].to_list(),
                               "asentamiento_id":diccionario["asentamiento_id"].to_list(),
                               "zona_asentamiento":diccionario["zona_asentamiento"].to_list(),
                               "esatado_id":diccionario["esatado_id"].to_list(),
                               "municipio_id":diccionario["municipio_id"].to_list()                 
                               }
                    return diccionario
                else:
                    diccionario = {"colonia_id":datos["colonia_id"].to_list(),
                               "codigo_postal_asentamiento":datos["codigo_postal_asentamiento"].to_list(),
                               "nombre_colonia":datos["nombre_colonia"].to_list(),
                               "tipo_asentamiento":datos["tipo_asentamiento"].to_list(),
                               "codigo_postal_administracion":datos["codigo_postal_administracion"].to_list(),
                               "clave_tipo_asentamiento":datos["clave_tipo_asentamiento"].to_list(),
                               "asentamiento_id":datos["asentamiento_id"].to_list(),
                               "zona_asentamiento":datos["zona_asentamiento"].to_list(),
                               "esatado_id":datos["esatado_id"].to_list(),
                               "municipio_id":datos["municipio_id"].to_list()                 
                               }
                    return diccionario
    ```

    

* Archivo **tablas.sql**: Archivo que contiene la definción pura de las tablas en SQL. En el se detalla que se crearon 3 tablas para simplicidad del modelo.

  * ```sql
    ---Tabla correspondiente a Estado
    CREATE TABLE estado(
        esatado_id serial primary key,
        nombre_enetidad character varying not null,
        clave_entidad integer not null
    );
    ---Tabla correspondiente al municipio
    CREATE TABLE municipio(
        municipio_id serial primary key,
        nombre_municipio character varying null,
        nombre_ciudad character varying null,
        clave_municipio integer not null,
        clave_ciudad integer null,
        esatado_id integer,
        CONSTRAINT esatado_id_fk FOREIGN KEY (esatado_id)
            REFERENCES estado (esatado_id)
    );
    
    ---Tabla correspondiente a la colonia
    CREATE TABLE colonia(
        colonia_id serial primary key,
        codigo_postal_asentamiento integer,
        nombre_colonia character varying null,
        tipo_asentamiento character varying null,
        codigo_postal_administracion integer,
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
    
    ```
    
    

El códgio se encuentran alojado en el siguiente servidor de Heroku: https://pruebatecnica7.herokuapp.com

El código también se encuentra alojado en el siguiente repositorio, donde está en una rama secundaria: 