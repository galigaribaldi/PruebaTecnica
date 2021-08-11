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

carga = ModelsData()
carga.drop_Tables()
carga.create_tables()
carga.delete_Info_Tables()
tuplas = CargaDatos()
#carga.selectEstado()