# -*- coding: utf-8 -*-

# Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que 
# incorpore la lectura de parámetros por línea de comando
# para que funcione lo llamo asi:
# python camion_commandline.py data/camion.csv


import csv
import sys

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        encabezados = next(f).split(',') 
        for linea in f:                 
            elementos_fila = linea.split(',')
            total = float(elementos_fila[1]) * float(elementos_fila[2])
            costo_total += total    
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
    print('Costo Total: ',costo_camion(nombre_archivo))
else:
    print('No se suministro archivo')