# -*- coding: utf-8 -*-

# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.

# Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        encabezados = next(f).split(',') 
        for linea in f:                 
            elementos_fila = linea.split(',')
            total = float(elementos_fila[1]) * float(elementos_fila[2])
            costo_total += total    
    return costo_total


def leer_camion(nombre_archivo):
    
    lista_dict = []
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            lista_dict.append(linea)
    return lista_dict

def leer_precios(nombre_archivo):
    
    with open(nombre_archivo, encoding='utf-8') as f:
        return dict(filter(None, csv.reader(f))) # Recuerde que d es un diccionario que contiene todos los valores de fruta:precio

data_precios = leer_precios('data/precios.csv')
data_camion = leer_camion('data/camion.csv')
dinero_ganado = 0

for each in data_camion:
    a_buscar = each.get('nombre')
    if a_buscar in data_precios:
        resultado = float(data_precios.get(a_buscar)) * float(each.get('cajones'))
        dinero_ganado += resultado

dinero_invertido = costo_camion('data/camion.csv')
ganancia = dinero_ganado - dinero_invertido

print(f'Tuve una ganancia de {ganancia:0.2f} pesos')