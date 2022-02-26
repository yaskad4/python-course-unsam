# Ejercicio 1.18
# Geringoso Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.


cadena = input('Cadena a convertir: ')
vocales = ['a','e','i','o','u','A','E','I','O','U']

nueva_cadena = []

for c in cadena:
    if c in vocales:
        c = c + 'p' + c
    nueva_cadena.append(c)

cadena_final = "".join(nueva_cadena)
print(cadena_final)

# Lo inverso, o sea imprimir cadena normal a partir de cadena geringosa

cad_geringoso = input("Decime una cadena geringosa: ")
cad_normal = []
indice = 0

for posicion in range(len(cad_geringoso) - 1):
    
    pos = posicion + indice
    
    if cad_geringoso[pos] in vocales and cad_geringoso[pos + 1] == 'p' and cad_geringoso[pos + 2] == cad_geringoso[pos]:
        cad_normal.append(cad_geringoso[pos])
        if pos <= (len(cad_geringoso) - 4):
            indice += 2
        else:
            break
    else:
        cad_normal.append(cad_geringoso[pos])
        
cad_original = "".join(cad_normal)
print(cad_original)      