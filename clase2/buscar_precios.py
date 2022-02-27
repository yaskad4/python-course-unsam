# -*- coding: utf-8 -*-
import csv


# Las siguientes 2 lineas permiten abrir el csv de los precios y convertir su contenido
# a un diccionario del tipo clave:valor, simplificando luego las tareas a realizar
# imprimir path actual  


with open('data/precios.csv', encoding='utf-8') as f:
    d = dict(filter(None, csv.reader(f))) # Recuerde que d es un diccionario que contiene todos los valores de fruta:precio

def buscar_fruta(fruta,d):
    # Funcion que busca el precio de determinda fruta o vegetal
    # Recibe la fruta a buscar (como cadena) y el diccionario donde estan guardadas la fruta:precio
    if fruta in d:
        print(f'Precio de {fruta}: ', d.get(fruta))
    else:
        print(f'La fruta, o verdura {fruta} no se encuentra en el listado')


fruta = input('Fruta o verdura a buscar: ')
buscar_fruta(fruta,d)
