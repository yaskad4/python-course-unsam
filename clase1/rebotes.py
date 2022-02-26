# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
# Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

high = 100
bounce = 3/5

for i in range(10):
    high *= bounce   # altura = altura * REBOTE
    print(f'Rebote # {i + 1} - {round(high,4)} metros')
