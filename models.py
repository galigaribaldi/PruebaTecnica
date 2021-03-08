server1 = 'hamburgo.myinfo.la'#,31433'
user1 = 'usrExamen'
passw1 = 'd08q23lnco82wNIUmdcaq9012.xJma'
db1 = 'EXAMEN'
puerto=31433

import pymssql

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

##Tabla Usuario
def createTableU():
    conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
    cursor = conn.cursor()  
    cursor.execute('''CREATE TABLE usuario_hgcg(
            usuario_id int PRIMARY KEY,
            telefono varchar(40),
            twitter varchar(40),
            facebook varchar(40),
            correo varchar(40),
            centro_acopio_hgcg_id int,
            CONSTRAINT fk_centro_acopio FOREIGN KEY (centro_acopio_hgcg_id) REFERENCES centro_acopio_hgcg (centro_acopio_hgcg_id)
        )''') 
    conn.commit()
    conn.close()

##Tabla ubicacion
def createTableUb():
    conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
    cursor = conn.cursor()  
    cursor.execute('''CREATE TABLE ubicacion_hgcg(
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
        )''') 
    conn.commit()
    conn.close()
    
#print("Creando tabla Centro de Acopio")
#createTableCA()
#print("Creando tabla Centro de User")
#createTableU()
#print("Creando tabla Centro de Ubicación")
#createTableUb()
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
#t = ((7,'s','s','s','s','s','s','s','s','s','s','s'), (8,'s','s','s','s','s','s','s','s','s','s','s'))
#insertCA(t)

def insertUs(tuples):
    conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
    cursor = conn.cursor() 
    query = """INSERT INTO usuario_hgcg(usuario_id, telefono,twitter, facebook,correo,centro_acopio_hgcg_id)
                   VALUES('%d','%s','%s','%s','%s','%d');"""
    query = """INSERT INTO usuario_hgcg(usuario_id, telefono,twitter, facebook,correo,centro_acopio_hgcg_id)
                   VALUES(%d,%s,%s,%s,%s,%d);"""
    #query=query%tuples
    print(query)
    cursor.executemany(query, tuples) 
    conn.commit()
    conn.close()
#t = ((1,'s','s','s','s',7), (2,'s','s','s','s',7))
#insertUs(t)

def insertUb(tuples):
    conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
    cursor = conn.cursor() 
    query = """INSERT INTO ubicacion_hgcg(ubicacion_id, numero_exterior,colonia, delegacion,ciudad,entidad,zona,direccion,latitud,altitud,link_maps,centro_acopio_hgcg_id)
                   VALUES('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%d');"""
    query = """INSERT INTO ubicacion_hgcg(ubicacion_id, numero_exterior,colonia, delegacion,ciudad,entidad,zona,direccion,latitud,altitud,link_maps,centro_acopio_hgcg_id)
                   VALUES(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d);"""
    #query=query%tuples
    print(query)
    cursor.executemany(query, tuples) 
    conn.commit()
    conn.close()
#t = ((4,'1','s','s','s','s','s','s','s','s','s',7), (5,'1','s','s','s','s','s','s','s','s','s',8))
#insertUb(t)

################consultas
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
#c = consultas()
#print(c)
def eliminar():
    conn = pymssql.connect(server=server1, user=user1, password=passw1, database=db1,port=puerto)
    cursor = conn.cursor() 
    ####
    query = """DELETE from usuario_hgcg;"""
    print(query)
    cursor.execute(query)
    ####
    ####
    query = """DELETE from ubicacion_hgcg;"""
    print(query)    
    cursor.execute(query)
    ####
    ####
    query = """DELETE from centro_acopio_hgcg;"""
    print(query)
    cursor.execute(query)
    ####
    conn.commit()
    conn.close()