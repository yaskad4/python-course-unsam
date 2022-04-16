def invertir_lista(lista):
    """ Ejercicio 4.5 Invertir lista.
        Parametros:
            lista(list): Lista a invertir
        Devuelve:
            invertida(list): Lista invertida
    """
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

if __name__ == '__main__':
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
    