def buscar_u_elemento(lista, elemento):
    """ Ejercicio 4.3 - Funcion que recibe una lista y un elemento, 
        y devuelve la posicion de la ultima aparicion de ese elemento, 
        o -1 si el elemento no pertenece a la lista"""
    for i in range(len(lista)-1,-1,-1):
        if lista[i] == elemento:
            return i # Si encuentra el elemento devuelvo la posicion
    return -1 # Si llega aca, es que recorriio toda la lista y no encontro el elemento

def buscar_n_elemento(lista, elemento):
    """ Ejercicio 4.3 - Funcion que recibe una lista y un elemento, 
        y devuelve el numero de veces que ese elemento esta en la lista"""
    cantidad_de_veces = 0
    for i in range(len(lista)-1):
        if lista[i] == elemento:
            cantidad_de_veces += 1 # Cada vez que lo encuentro incremento el contador
    return cantidad_de_veces

def maximo(lista):
    """ Ejercicio 4.4 - Funcion que devuelve el maximo de una lista, 
        esta debe no ser vacia y de numeros enteros"""
    m = lista[0]
    if not bool(lista): # Si la lista esta vacia devuelvo el mensaje de que esta vacia
      return 'La lista es vacia'
    for e in lista:
        if not isinstance(e, int): #comprobando que todos los elementos de la lista sean enteros
            return 'La lista contiene elementos que no son numeros enteros'
        if e > m:
            m = e
    return m

def minimo(lista):
    """ Ejercicio 4.4 - Funcion que devuelve el minimo de una lista, 
        esta debe no ser vacia y de numeros enteros"""
    # Muy similar a la funcion maximo
    m = lista[0]
    if not bool(lista):
      return 'La lista es vacia'
    for e in lista:
        if not isinstance(e, int):
            return 'La lista contiene elementos que no son numeros enteros'
        if e < m:
            m = e
    return m



if __name__ =='__main__':
    print(buscar_u_elemento([1,2,3,2,3,4],5))
    print(buscar_n_elemento([1,2,3,2,3,4],2))
    print(maximo([-1,-5,-2,-8, -5]))
    print(minimo([-1,-5,-2,-8, -5]))