# PruebaTecnica

Este repositorio contiene el código solciitado como pueba técnica, a continuación se explica a mayor detalle como es que está compuesto:

* Archivo **models.py**: En este archivo se detallan las funciones que hacen psoible lña conección a la base de datos y por lo tanto, las operaciones SQL necesarias para la *inserción*, *creación* y *consulta* de datos. **Este archivo funciona gracias a la librería *pymssql***

  * INSERT: 

    ```python
    def insertCA(tuples):
        conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
        cursor = conn.cursor() 
        query = """INSERT INTO centro_acopio_hgcg(centro_acopio_hgcg_id, nombre_centro_acopio,tipo_ca, necesidades,horario,tipo_detalles,
                       estatus,verifica,fecha_creacion,ultima_actualizacion,actualiza,nota_actualiza)
                       VALUES('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"""
        query = """INSERT INTO centro_acopio_hgcg(centro_acopio_hgcg_id, nombre_centro_acopio,tipo_ca, necesidades,horario,tipo_detalles,
                       estatus,verifica,fecha_creacion,ultima_actualizacion,actualiza,nota_actualiza)
                       VALUES(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        #query=query%tuples
        print(query)
        cursor.executemany(query, tuples) 
        conn.commit()
        conn.close()
    t = ((7,'s','s','s','s','s','s','s','s','s','s','s'), (8,'s','s','s','s','s','s','s','s','s','s','s'))
    insertCA(t)
    ```

  * CREATE: 

    ```python
    def createTableCA():
        conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
        cursor = conn.cursor()  
        cursor.execute('''CREATE TABLE centro_acopio_hgcg(
                centro_acopio_hgcg_id int PRIMARY KEY,
                nombre_centro_acopio  varchar(40),
                tipo_ca varchar(40),
                necesidades varchar(200),
                horario varchar(40),
                tipo_detalles varchar(40),
                estatus varchar(40),
                verifica varchar(40),
                fecha_creacion varchar(40),
                ultima_actualizacion varchar(40),
                actualiza varchar(200),
                nota_actualiza varchar(200)
            )''') 
        conn.commit()
        conn.close()
    
    ```

    

  * SELECT:

    ```python
    def consultas():
        conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
        cursor = conn.cursor() 
        ####
        query = """SELECT count(*) from centro_acopio_hgcg;"""
        print(query)
        cursor.execute(query)
        c = cursor.fetchall()
        ####
        ####
        query = """SELECT count(*) from usuario_hgcg;"""
        print(query)
        cursor.execute(query)
        c1 = cursor.fetchall()
        ####
        ####
        query = """SELECT count(*) from ubicacion_hgcg;"""
        print(query)    
        cursor.execute(query)
        c2 = cursor.fetchall()
        ####        
        conn.commit()
        conn.close()
        return c[0][0],c1[0][0],c2[0][0]
    ```

    

* Archivo **lector.py**: En este archivo se detalla la lectura y transformación de los datos, para ell se utiliza la librería *pandas*, la que nos ayuda a dividir el archivo en subparte y transformarla a tuplas.

  * ```python
    def cargaU(nombreArchivo):
        xls = pd.ExcelFile(nombreArchivo)
        Carga = xls.parse('Centros de Acopio - Colaborativ')
        Carga = Carga.fillna(0)
        ids = (Carga['id'])
        id2 = (Carga['ID2'])#; id2 = int(id2[1:])+100
        telef = (Carga['Teléfono'])
        twitt = (Carga['Twitter'])
        fb = (Carga['Facebook'])
        correo = (Carga['Correo'])
        listaF = []
        listaA = []
        for i in range(len(ids)):
            if ids[i]>0:
                listaA.append(i);listaA.append(str(telef[i]))
                listaA.append(str(twitt[i]));listaA.append(str(fb[i]))
                listaA.append(str(correo[i]));listaA.append(ids[i])
                for j in range(len(listaA)):
                    if type(listaA[j]) == str:
                        if len(listaA[j])>39:
                            listaA[j]=listaA[j][:39]                        
                listaF.append(tuple(listaA))
                listaA = []
                
        return tuple(listaF)
    
    #c = cargaU('datos.xlsx')
    #print(c)
    ```

    

* Archivo **main.py**: Este es el archivo principal, el que se debe de correr para poder insertar y consultar si los resultados son correctos. **Es necesario tener los demás archivos al mismo nivel para que se oueda estructurar de forma correcta**

  * ```python
    import models as coneccion
    import lector as lc
    coneccion.eliminar()
    c = lc.cargaCA('datos.xlsx')
    coneccion.insertCA(c)
    
    c = lc.cargaU('datos.xlsx')
    coneccion.insertUs(c)
    
    c = lc.cargaUb('datos.xlsx')
    coneccion.insertUb(c)
    
    print("Comprobando carga de datos")
    c = coneccion.consultas()
    print("Registros finales: ", c )
    ```

    

* Archivo **tablas.sql**: Archivo que contiene la definción pura de las tablas en SQL. En el se detalla que se crearon 3 tablas para simplicidad del modelo.

  * ```sql
    CREATE TABLE centro_acopio_hgcg(
        centro_acopio_hgcg_id int PRIMARY KEY,
        nombre_centro_acopio  varchar(200),
        tipo_ca varchar(40),
        necesidades varchar(200),
        horario varchar(40),
        tipo_detalles varchar(200),
        estatus varchar(40),
        verifica varchar(40),
        fecha_creacion varchar(40),
        ultima_actualizacion varchar(200),
        actualiza varchar(200),
        nota_actualiza varchar(200)
    );
    CREATE TABLE usuario_hgcg(
        usuario_id int PRIMARY KEY,
        telefono varchar(40),
        twitter varchar(40),
        facebook varchar(200),
        correo varchar(200),
        centro_acopio_hgcg_id int,
        CONSTRAINT fk_centro_acopio FOREIGN KEY (centro_acopio_hgcg_id) REFERENCES centro_acopio_hgcg (centro_acopio_hgcg_id)
    );
    CREATE TABLE ubicacion_hgcg(
        ubicacion_id int primary key,
        numero_exterior varchar(40),
        colonia  varchar(200),
        delegacion varchar(200),
        ciudad varchar(200),
        entidad varchar(200),
        zona varchar(200),
        direccion varchar(200),
        latitud varchar(200),
        altitud varchar(200),
        link_maps varchar(200),
        centro_acopio_hgcg_id int,
        CONSTRAINT fk_centro_acopio_fk FOREIGN KEY (centro_acopio_hgcg_id) REFERENCES centro_acopio_hgcg (centro_acopio_hgcg_id)            
    );
    ```

    