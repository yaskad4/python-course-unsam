# -*- coding: utf-8 -*-

# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        encabezados = next(f).split(',') # Esto es para no tener en cuenta los encabezados del csv, ya que no contienen datos a calcular
        for linea in f:                 # A partir de aqui recorremos cada linea del csv y calculamos el total
            elementos_fila = linea.split(',')
            total = float(elementos_fila[1]) * float(elementos_fila[2])
            costo_total += total    # En este punto vamos incrementando el costo_total, que sera el dato a devolver por la funcion
    return costo_total

print(f"El total del costo del camion es {costo_camion('data/camion.csv')} pesos")

