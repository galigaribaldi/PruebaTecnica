import pandas as pd
def cargaCA(nombreArchivo):
    xls = pd.ExcelFile(nombreArchivo)
    Carga = xls.parse('Centros de Acopio - Colaborativ')
    Carga = Carga.fillna(0)
    ids = (Carga['id'])
    nombre = (Carga['Nombre del centro de acopio'])
    tipo_ca = (Carga['Tipo'])
    necesidades = (Carga['Necesidades'])
    horario = (Carga['Horarios'])
    tipo_detalles = (Carga['Tipo de Centro de Acopio'])
    est = (Carga['Estatus'])
    verifica = (Carga['Verificado por'])
    fecha_creacion = (Carga['Fecha de creación'])
    ultima_actualizacion = (Carga['Última actualización'])
    actu_po = (Carga['Actualizado por'])
    nota_actualiza = (Carga['Nota actualización'])
    listaF = []
    listaA = []
    for i in range(len(ids)):
        if ids[i]>0:
            listaA.append(ids[i]);listaA.append(str(nombre[i]))
            listaA.append(str(tipo_ca[i]));listaA.append(str(necesidades[i]))
            listaA.append(str(horario[i]));listaA.append(str(tipo_detalles[i]))
            listaA.append(str(est[i]));listaA.append(str(verifica[i]))
            listaA.append(str(fecha_creacion[i]));listaA.append(str(ultima_actualizacion[i]))
            listaA.append(str(actu_po[i]));listaA.append(str((nota_actualiza[i])))
            for j in range(len(listaA)):
                if type(listaA[j]) == str:
                    if len(listaA[j])>39:
                        listaA[j]=listaA[j][:39]                        
            listaF.append(tuple(listaA))
            listaA = []
    return tuple(listaF)

#c = cargaCA('datos.xlsx')
#print(c)
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

def cargaUb(nombreArchivo):
    xls = pd.ExcelFile(nombreArchivo)
    Carga = xls.parse('Centros de Acopio - Colaborativ')
    Carga = Carga.fillna(0)
    ids = (Carga['id'])
    id2 = (Carga['ID2'])#; id2 = int(id2[1:])+101
    num_ext = (Carga['numero_exterior'])
    colonia = (Carga['colonia'])
    deleg = (Carga['delegacion o municipio'])
    ciudad = (Carga['Ciudad'])
    ent = (Carga['Entidad'])
    zon = (Carga['Zona'])
    direccion = (Carga['Dirección (agregada)'])
    lat = (Carga['lat'])
    alt = (Carga['lon'])
    link = (Carga['link_google_maps'])
    listaF = []
    listaA = []
    for i in range(len(ids)):
        if ids[i]>0:
            listaA.append(i);listaA.append(str(num_ext[i]))
            listaA.append(str(colonia[i]));listaA.append(str(deleg[i]))
            listaA.append(str(ciudad[i]));listaA.append(str(ent[i]))
            listaA.append(str(zon[i]));listaA.append(str(direccion[i]))
            listaA.append(str(lat[i]));listaA.append(str(alt[i]))
            listaA.append(str(link[i]));listaA.append(ids[i])
            for j in range(len(listaA)):
                if type(listaA[j]) == str:
                    if len(listaA[j])>39:
                        listaA[j]=listaA[j][:39]                        
            listaF.append(tuple(listaA))
            listaA = []
    return tuple(listaF)

#c = cargaUb('datos.xlsx')
#print(c)