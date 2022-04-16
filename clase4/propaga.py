def propagarmio(lista):
    """ Ejercicio 4.6 Propagacion. Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

    Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py."""
        
    largo_lista = len(lista)
    for i, e in enumerate(lista):
        
        if e == 1 and  (0 <= i < largo_lista):
            #propaga derecha
            for derecha in range(i + 1, largo_lista): # va del siguiente a la derecha hasta el final 
                if lista[derecha] == -1: # este es el unico que me interesa, ya que siempre que sea 0 o 1 lo dejo encendido
                    break
                lista[derecha] = 1
            #propaga izquierda 
            for izquierda in range(i - 1, -1, -1):  # va desde el anterior hasta el primero de la lista
                if lista[izquierda] == -1:
                    break
                lista[izquierda] = 1
    return lista

def propagar(unosyceros):
    n = len(unosyceros)
    for i in range(n-1):
        if unosyceros[i] == 1:
            if unosyceros[i+1] == 0:
                unosyceros[i+1] = 1
    for j in range(n-1,0,-1):
        if unosyceros[j] == 1:
            if unosyceros[j-1] == 0:
                    unosyceros[j-1] = 1
    return unosyceros
                        




if __name__ == '__main__':
    lista = [1,-1,0,1]
    print(lista)
    print(propagar(lista))
    print(propagarmio(lista))