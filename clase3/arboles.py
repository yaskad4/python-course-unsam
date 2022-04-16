# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:02:00 2021

@author: Kadyr Valdes
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

lista_dict = []


def leer_arboles(nombre_archivo):
    """" Ejercicio 4.15
    Basándote en la función leer_parque(nombre_archivo, parque) 
    del Ejercicio 3.18, escribí otra leer_arboles(nombre_archivo) que lea el 
    archivo indicado y devuelva una lista de diccionarios con la información 
    de todos los árboles en el archivo. La función debe devolver una lista 
    conteniendo un diccionario por cada árbol con todos los datos.
    """
    linea = {}
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            # print(linea)
            lista_dict.append(linea)
    arboleda = []
    for cada in lista_dict:
        arboleda.append(cada)
    return arboleda  # Devuelve una lista de los arboles del parque


def altura_y_diametro(arboleda, especie):
    """ Ejercicio 4.16 y 1.17 Recibe la variable arboleda y una especie 
    especifica y devuelve una lista de tuplas conteniendo altura y diametro
    """
    H = [float(arbol['altura_tot'])
         for arbol in arboleda if arbol['nombre_com'] == especie]
    g = [float(arbol['diametro'])
         for arbol in arboleda if arbol['nombre_com'] == especie]
    j = (zip(H, g))
    G = []
    for cada in j:
        G.append(cada)
    return G


def medidas_de_especies(especies, arboleda):
    """ Ejercicio 4.18 Recibe una lista con especies y los datos de los 
    arboles, y devuelve un diccionario con la clave especie y la lista de 
    tuplas de esa especie correspondiente a la altura y al diametro de todos 
    los arboles
    """
    diccionario_especies = {}
    for cada in especies:
        gg = altura_y_diametro(arboleda, cada)
        diccionario_especies[cada] = gg
    return diccionario_especies


def plotear_alturas(nombre_archivo, especie):
    """EJERCICIO 5.25"""
    arboleda = leer_arboles(nombre_archivo)
    altos = [float(arbol['altura_tot'])
             for arbol in arboleda if arbol['nombre_com'] == especie]
    plt.hist(altos, bins=50)


def scatter_hd(lista_de_pares):
    """EJERCICIO 5.26"""
    alturas_y_diametros = np.array(lista_de_pares)
    diametros = alturas_y_diametros[:, 0]
    alturas = alturas_y_diametros[:, 1]
    plt.figure()
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.scatter(diametros, alturas, alpha=0.3)
    plt.show()


def scatter_hd_multiple(lista_de_pares, especie):
    """EJERCICIO 5.27"""
    alturas_y_diametros = np.array(lista_de_pares)
    diametros = alturas_y_diametros[:, 0]
    alturas = alturas_y_diametros[:, 1]
    maxima_altura = max(alturas)
    maximo_diametro = max(diametros)
    print(maxima_altura, maximo_diametro)
    plt.figure()
    plt.xlim(0, maximo_diametro)
    plt.ylim(0, maxima_altura)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    titulo = "Relación diámetro-alto para " + especie
    plt.title(titulo)
    plt.scatter(diametros, alturas, alpha=0.3)
    plt.show()


if __name__ == '__main__':
    nombre_archivo = os.path.join(
        'data', 'arbolado-en-espacios-verdes.csv')
    especie = 'Jacarandá'
    plotear_alturas(nombre_archivo, especie)
    arboleda = leer_arboles(nombre_archivo)

    lista_de_pares = altura_y_diametro(arboleda, especie)
    # print(lista_de_pares)

    #print(altura_y_diametro(arboleda, especie))
    #alturas_y_diametros = np.array(altura_y_diametro(arboleda, especie))
    # print(alturas_y_diametros)
    #diametros = alturas_y_diametros[:,0]
    #alturas = alturas_y_diametros[:,1]
    # print(diametros)
    # print(alturas)

    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    # print(medidas)
    # scatter_hd(lista_de_pares)
    for cada in especies:
        scatter_hd_multiple(medidas[cada], cada)