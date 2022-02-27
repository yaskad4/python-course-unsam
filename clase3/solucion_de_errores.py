#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de semantico ya que no tiene en consideracion las A mayusculas, ademas el else esta mal planteado, ya que la funcion finaliza en el primer caracter que no sea a, devolviendo falso.
#    Lo corregí cambiando añadiendo la funcion lower al string recibido, y returnando falso si recorri todos los caractares y no encontre ninguna a
#    A continuación va el código corregido

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de tipo sintactico, faltan los : en la definicion de funcion, en el while y en el if, ademas se returna False no Falso. Tambien para comparar se utiliza == . Tambien tenemos el error de tipo semantico que no tiene en cuenta las mayusculas
# Lo corregí cambiando añadiendo la funcion lower al string recibido, y colocando los : adecuadamente. Tambien se cambio = por ==

def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era en tiempo de ejecucion, ya que la funcion espera una cadena y no un numero
#Lo corregí cambiando a string si lo que se recibe en expresion no es una cadena

def tiene_uno(expresion):
    if type(expresion) != 'str':
        expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error es semantico, ya que la funcion no retorna ningun valor, por eso el None como resultado.
#Lo corregí modificando la funcion para que devuelva la suma de a + b
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: El error es en tiempo de ejecucion, ya que la funcion devuelve una lista incorrecta.
#Lo corregí colocando registro = {} en el lugar correcto, justo antes de usarlo en el ciclo for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
        
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)