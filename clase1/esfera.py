# Ejercicio 1.13
# Calcular el volumen de una esfera, dado su radio.

import math

ratio = float(input("Ingrese el radio de la esfera: 12"))
volume = 4 / 3 * math.pi * (ratio ** 3)

print(f'El volumen de la esfera es {volume}')