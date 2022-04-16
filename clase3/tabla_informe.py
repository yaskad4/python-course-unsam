# -*- coding: utf-8 -*-
import csv
import decimal

def leer_camion(nombre_archivo):
    """ Funcion que devuelve una lista de diccionarios con todo lo que contiene el camion,
        o sea fruta o vegetal, luego numero de cajones, y finalmente precio"""
    
    lista_dict = []
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            lista_dict.append(linea)
    return lista_dict


def leer_precios(nombre_archivo):
    """ Funcion que devuelve un diccionario con la key fruta o vegetal, y el valor precio """
    
    with open(nombre_archivo, encoding='utf-8') as f:
        return dict(filter(None, csv.reader(f))) 


def hacer_informe(camion,precios):
    """ Funcion que recibe la lista de diccionarios, camion, y el diccionario precios,
        y devuelve una lista con cada una de las filas del informe solicitado"""
    
    report = []
    for each in camion:
        registro = {}
        encabezado = ['Nombre','Cajones','Precio','Cambio']
        a_buscar = each.get('nombre')
        if a_buscar in precios:
            registro[encabezado[0]] = a_buscar
            registro[encabezado[1]] = each.get('cajones')
            registro[encabezado[2]] = float(precios.get(a_buscar)) - (float(precios.get(a_buscar)) - float(each.get('precio')))
            registro[encabezado[3]] = (float(precios.get(a_buscar)) - float(each.get('precio')))
            report.append(registro)
    return report


if __name__ == '__main__':
        
    camion = leer_camion('data/camion.csv')
    precios = leer_precios('data/precios.csv')
    print('XXXXX', camion)
    print('XXXXX', precios)
    informe = hacer_informe(camion, precios)
    print(type(informe))
    # Impresion en pantalla del informe final

    print(
    '''Nombre        Cajones    Precio     Cambio
    ---------    ---------    -------   ------''')
    for r in informe:
        nombre = r.get('Nombre')
        cajones = int(r.get('Cajones'))
        precio = float(r.get('Precio'))
        precio = decimal.Decimal(precio).quantize(decimal.Decimal('0.00'),rounding=decimal.ROUND_CEILING)
        precio = ('$' + str(precio))
        cambio = float(r.get('Cambio'))
        print(f'{nombre:<10s}{cajones:>10d} {precio:>10s}{cambio:10.2f}')