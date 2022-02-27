
# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso. 
# Probá tu función para la lista ['banana', 'manzana', 'mandarina'].

def conversor_geringoso(texto):
    
    VOCALES = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    nueva_cadena = []
    for c in texto:
        if c in VOCALES:
            c = c + 'p' + c
        nueva_cadena.append(c)
    return ''.join(nueva_cadena)

lista = ['banana', 'manzana', 'mandarina']
lista_geringoso = []
s = {}

cantidad = len(lista)

for i in range(cantidad):
    s[lista[i]] = conversor_geringoso(lista[i])

print(s)


