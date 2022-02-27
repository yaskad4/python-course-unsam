# -*- coding: utf-8 -*-

#El archivo ../Data/precios.csv contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:
#"Lima",40.22
# "Uva",24.85
# "Ciruela",44.85
# "Cereza",11.27
# "Frutilla",53.72
# Escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.

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
