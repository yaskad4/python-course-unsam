# -*- coding: utf-8 -*-

# informe del costo del camion 
import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

print(costo_camion('data/fecha_camion.csv'))
print(costo_camion('data/camion.csv'))

# fijate que funciona para ambos archivos a pesar de que tienen estructura muy diferente
