# lectura de archivos
'''
with open('data/movimientos.csv','r') as resultado:
    leer = resultado.read()
    print( type(leer) )
'''
#otro ejemplo
'''
resultado = open('data/movimientos.csv','r')
lectura = resultado.readlines()
print(type(lectura))
'''
'''
import csv

midato = []
mifichero = open('data/movimientos.csv','r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')

print(type(lectura))
for items in lectura:
    print(items)
    midato.append(items)

print("mi lista:",midato)
'''
#ejemplo de registro de datos en csv
'''
import csv
mifichero = open('data/movimientos.csv','a',newline='')
lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
lectura.writerow(['24/04/2023','compra de lentes','-40'])

mifichero.close()
'''
'''
datos=[('fecha', '2023-04-25'), ('concepto', 'compra de gorro'), ('monto', '3212')]
print(datos[0][1])
'''

#para obtener la fecha actual
from datetime import date
print(type( str(date.today()) ))

print("fecha de hoy: ",date.today())