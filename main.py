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