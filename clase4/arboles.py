# -*- coding: utf-8 -*-

import csv
from collections import Counter
import statistics as stats

lista_dict = []


#---------------------------------------------------------------------
def leer_arboles(nombre_archivo):
    """" Ejercicio 4.15
    Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios con la información de todos los árboles en el archivo. La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos.
    """
    linea = {}
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            #print(linea)
            lista_dict.append(linea)
    arboleda = []
    for cada in lista_dict:
        arboleda.append(cada)
    #print(arboleda)
    return arboleda # Devuelve una lista de los arboles del parque

#---------------------------------------------------------------------
def altura_y_diametro(arboleda, especie):
    """ Ejercicio 4.16 y 1.17 Recibe la variable arboleda y una especie especifica y devuelve una lista de tuplas conteniendo altura y diametro
    """
    H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie]
    g=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie]
    j = (zip(H,g))
    G = []
    for cada in j:
        G.append(cada)
    return G


#---------------------------------------------------------------------
def medidas_de_especies(especies, arboleda):
    """ Ejercicio 4.18 Recibe una lista con especies y los datos de los arboles, y devuelve un diccionario con la clave especie y la lista de tuplas de esa especie correspondiente a la altura y al diametro de todos los arboles
    """
    diccionario_especies = {}
    for cada in especies:
        gg = altura_y_diametro(arboleda,cada)
        diccionario_especies[cada] = gg
    return diccionario_especies
    
#---------------------------------------------------------------------
if __name__ == '__main__':
    arboleda = leer_arboles('data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá'] 
    print(medidas_de_especies(especies, arboleda))